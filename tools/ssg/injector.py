from datetime import datetime
from pathlib import Path
import re

from tools import COMPONENTS_PATH, vlog

# Injects HTML into the pseudo-element components
def inject_html(updated_files: tuple[str]) -> None:
    # Read all components
    components = {
        str(p).replace("/", ".").replace("src.ssg-components.", "").replace(".html", "")
        : p.read_text()
            .replace("%%TIMESTAMP%%", datetime.now().strftime("%b. %Y"))
        for p in Path(COMPONENTS_PATH).rglob("*")
        if p.is_file()
    }

    # Find each HTML file in the subtree
    html_files = tuple( [Path(f) for f in updated_files if f.endswith(".html")] )

    for file in html_files:
        # Replace all pseudo-elements with their HTML components
        body = file.read_text()

        # Regex replace elements
        def comp(m: re.Match) -> str:
            # Fix indents
            indent = m.group(1)
            return indent + components[ m.group(2) ].replace("\n", f"\n{indent}")

        body = re.sub(
            rf"^(\s*)<\s*({ '|'.join([k for k in components.keys()]) })\s*\/\s*>",
            comp,
            body,
            flags=re.MULTILINE
        )

        # Write back to file
        file.write_text(body)

        # Log if verbose
        vlog(f"Built ./{file}")
