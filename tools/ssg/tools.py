from datetime import datetime, timezone
import os
import pathlib
import re
import requests
import shutil
from sys import argv

SRC_PATH  = "./src/"
DEST_PATH = "./public/"
COMPONENTS_PATH = "./src/ssg-components/"

# Check if an argument is set
def isarg(c: str) -> bool:
    if len(argv) <= 1: return False
    return argv[1][0] == "-" and c in argv[1]

# Prints all arguments to console with a debug message,
#   IF the -v flag is set (for verbose logging)
def vlog(*args: list[any]) -> None:
    if isarg("v"):
        log(*args)

# Prints all arguments to console with a debug message
def log(*args: list[any]) -> None:
    if isarg("c"): # Colored ANSI output
        print("\033[96m\033[1m[INFO]\033[0m", *args)
    else:
        print("[INFO]", *args)

# Prints all arguments to console with a warning message
def warn(*args: list[any]) -> None:
    if isarg("c"): # Colored ANSI output
        print("\033[93m\033[1m[WARN]\033[0m", *args)
    else:
        print("[WARN]", *args)

# Prints all arguments to console with an error message
def err(*args: list[any]) -> None:
    if isarg("c"): # Colored ANSI output
        print("\033[91m\033[1m[ERROR]\033[0m", *args)
    else:
        print("[ERROR]", *args)

# File copy helpers
_latest_ssg_comp_mtime = -1
_files_copied = []

# Copies a file & records its path
def copy(src: str, dest: str) -> str:
    _files_copied.append(dest)
    return shutil.copy2(src, dest)

# Copies a file if it's newer than what's in the dest directory
def copy_if_newer(src: str, dest: str) -> str:
    if os.path.exists(dest):
        src_mtime = os.path.getmtime(src)
        dest_mtime = os.path.getmtime(dest)

        # Check if this is an HTML file and the ssg-components directory has new content
        is_html_with_old_comps = dest.endswith(".html") and _latest_ssg_comp_mtime > dest_mtime

        # Compare mod timestamps
        if dest_mtime >= src_mtime and not is_html_with_old_comps:
            return dest
        else:
            vlog(f"Copied {src} --> {dest}")

    # Base case, copy as usual
    _files_copied.append(dest)
    return shutil.copy2(src, dest)

# Used by shutil.copytree to ignore the root ssg-components directory
def ignore_root_ssg_components(dir: str, contents: any) -> None:
    if os.path.abspath(dir) == os.path.abspath(SRC_PATH):
        return {"ssg-components"}
    return set()

# Used to copy the new source
def copy_source() -> tuple[str]:
    if os.path.exists(DEST_PATH):
        # Handle copies
        if isarg("f"):
            # Purge all
            shutil.rmtree(DEST_PATH)

            # Copy new
            shutil.copytree(SRC_PATH, DEST_PATH, ignore=ignore_root_ssg_components, copy_function=copy)
            log("Cleaned existing build content.")
        else:
            # Determine mtime of newest ssg component
            global _latest_ssg_comp_mtime
            _latest_ssg_comp_mtime = max(
                os.path.getmtime(str(p.resolve())) for p in pathlib.Path(COMPONENTS_PATH).rglob("*")
            )

            # Copy only updated
            shutil.copytree(SRC_PATH, DEST_PATH, ignore=ignore_root_ssg_components, copy_function=copy_if_newer, dirs_exist_ok=True)

            if len(_files_copied) > 0:
                log("Updated modified build content.")
            else:
                log("Already up-to-date (-f to force rebuild).")
                exit(0)
    else:
        # Initial copy
        shutil.copytree(SRC_PATH, DEST_PATH, ignore=ignore_root_ssg_components, copy_function=copy)
    
    # Return updated files
    return tuple(_files_copied)

# Creates public/sitemap.xml with update timestamps for all HTML files
def build_sitemap(files: tuple[str]) -> None:
    # Remove any existing ones
    sitemap_path = "./public/sitemap.xml"
    
    with open(sitemap_path, "w") as f:
        # Append header
        f.write(
            """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n"""
        )

        # Get mod time of all files
        for file in files:
            # Determine "pretty" path (remove ./public and index.html)
            pretty_path = file[(2 if file.startswith("./") else 0):][7:] \
                .replace("index.html", "")

            if pretty_path == "404.html": continue

            # Calculate index priority
            priority = max(0.2, 1 - 0.2 * pretty_path.count("/"))

            # Determine timestamp
            mtime = os.path.getmtime(file)
            dt = datetime.fromtimestamp(mtime, tz=timezone.utc).replace(microsecond=0)
            timestamp = dt.isoformat()

            # Write
            f.write(f"""    <url>
        <loc>https://wowtravis.com/{pretty_path}</loc>
        <lastmod>{timestamp}</lastmod>
        <priority>{priority:.2f}</priority>
    </url>\n""")

        # Close sitemap
        f.write("</urlset>\n")

# Simple HTML minifier
def minify_html(text: str) -> str:
    # Remove comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # Strip whitespace
    text = re.sub(r">\s+<", "><", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# Simple CSS minifier
def minify_css(text: str) -> str:
    # Remove comments
    text = re.sub(r"\/\*.*?\*\/", "", text, flags=re.DOTALL)

    # Strip whitespace
    # Remove unnecessary whitespace around symbols
    text = re.sub(r"\s*{\s*", "{", text)
    text = re.sub(r"\s*}\s*", "}", text)
    text = re.sub(r"\s*;\s*", ";", text)
    text = re.sub(r"\s*:\s*", ":", text)
    text = re.sub(r"\s*,\s*", ",", text)

    # Remove final semicolon before }
    text = re.sub(r";}", "}", text)

    # Collapse remaining whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()

# Simple JS minifier
def minify_js(text: str) -> str:
    # Remove comments
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    text = re.sub(r"//.*", "", text)

    # Remove whitespace around symbols
    text = re.sub(r"\s*([{};,:=+\-*/()<>])\s*", r"\1", text)

    # Remove remaining whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()

# Minifies HTML, CSS, and JS files in-place
def minify() -> None:
    # Get files
    html_files = tuple( [p for p in pathlib.Path(DEST_PATH).rglob("*.html")] )
    css_files = tuple( [p for p in pathlib.Path(DEST_PATH).rglob("*.css")] )
    js_files = tuple( [p for p in pathlib.Path(DEST_PATH).rglob("*.js")] )

    # HTML files
    for file in html_files:
        # Read & minify
        text = file.read_text()
        text = minify_html(text)

        # Write (truncated)
        with open(file, "w") as f:
            f.write(text)

    # CSS files
    for file in css_files:
        # Read & minify
        text = file.read_text()
        text = minify_css(text)

        # Write (truncated)
        with open(file, "w") as f:
            f.write(text)

    # JS files
    for file in js_files:
        # Read & minify
        text = file.read_text()
        text = minify_js(text)

        # Write (truncated)
        with open(file, "w") as f:
            f.write(text)
    
    log("Minified all HTML, CSS, and JS files")

# Fetches robots.txt
def fetch_robots() -> None:
    # Get release info
    api_url = "https://api.github.com/repos/ai-robots-txt/ai.robots.txt/releases/latest"
    res = requests.get(api_url)
    res.raise_for_status()
    data = res.json()

    # Extract download URL
    download_url = data["assets"][0]["browser_download_url"]

    # Download the file
    file_response = requests.get(download_url)
    file_response.raise_for_status()

    with open("public/robots.txt", "wb") as f:
        f.write(file_response.content)
