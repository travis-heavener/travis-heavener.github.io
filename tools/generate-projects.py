import json
import os

from util import *

def gen_project_section(data: any, first_row: bool) -> str:
    s = indent(3) + """<div class="section-wrapper">\n""" \
            + indent(4) + f"""<a href="#{data['year']}"><img src="/res/icons/hyperlink.svg" alt="Hyperlink icon."></a>\n""" \
            + indent(4) + f"""<h2 id="{data['year']}">{data['year']}</h2>\n""" \
            + indent(4) + f"""<img class="dropdown-icon{' active' if first_row else ''}" src="/res/icons/dropdown.svg" alt="Dropdown icon." tabindex="0">\n""" \
        + indent(3) + "</div>\n"

    # Add projects row
    s += indent(3) + f"""<div class="projects-row{'' if first_row else ' hidden'}">\n"""

    # Add each project
    for project in data["projects"]:
        s += indent(4) + """<div class="project-div">\n"""

        # Add images
        if len(project["imgs"]) == 3:
            s += indent(5) + """<div class="slideshow-3">\n"""

            for img in project["imgs"]:
                s += indent(6) + f"""<img class="project-img" loading="{img['loading']}" {'fetchpriority=\"high\"' if img['loading'] == 'eager' else ''} src="{img['src']}" alt="{img['alt']}">\n"""

            s += indent(5) + """</div>\n"""
        else:
            img = project["imgs"][0]
            s += indent(5) + f"""<img class="project-img" loading="{img['loading']}" {'fetchpriority=\"high\"' if img['loading'] == 'eager' else ''} src="{img['src']}" alt="{img['alt']}">\n"""

        # Add title
        if project["href"] is not None:
            s += indent(5) + f"""<h3><a href="{project['href']}">{project['title']}</a></h3>\n"""
        else:
            s += indent(5) + f"""<h3>{project['title']}</h3>\n"""

        # Add description
        s += indent(5) + f"""<p>{project['desc']}</p>\n"""

        s += indent(4) + """</div>\n"""

    # Close projects row
    s += indent(3) + """</div>\n"""

    return s

def gen_projects_table(data: any, body: str) -> str:
    # Generate table
    rows = ""
    for i, year in enumerate(data):
        if i == 0: # Start of table
            rows += "│     %E├──────┬──────────────────────┬────────────────────────────────────────────────────────┤%A     │\n"

        for j, project in enumerate(year["projects"]):
            r = "│     "
            r += "%E│ %O" + (year['year'] if j == 0 else "%A    ") + " %E│ %P" + pad_right(project["title"], max_len=20)
            r += " %E│ %Q" + pad_right(project["shortDesc"], max_len=55) + "%E│%A"
            r += "     │\n"
            rows += r

        if i+1 < len(data): # Not at end yet
            rows += "│     %E├──────┼──────────────────────┼────────────────────────────────────────────────────────┤%A     │\n"
        else: # End of table (no newline)
            rows += "│     %E└──────┴──────────────────────┴────────────────────────────────────────────────────────╯%A     │"

    # Insert projects table
    return body.replace("%%PROJECTS_TABLE%%", rows)

def gen_featured_project(data: any, body: str) -> str:
    # Find desired project
    featured_year = [y for y in data if y["year"] == "2025"][0]
    project = [p for p in featured_year["projects"] if p["title"] == "Mercury"][0]

    # Replace info
    body = body.replace("%%FEATURED_NAME%%", "%O" + pad_right(project["title"], max_len=36) + "%A")
    body = body.replace("%%FEATURED_HREF%%", "%P" + pad_right(project["href"], max_len=36) + "%A")

    # Replace description lines
    lines = [project["desc"], "", ""]
    if len(lines[0]) > 36:
        lines[0], lines[1] = overflow_lines(lines[0])

        if len(lines[1]) > 36:
            lines[1], lines[2] = overflow_lines(lines[1])

            if len(lines[2]) > 36:
                lines[2] = lines[2][:33] + "..."

    body = body.replace("%%FEATURED_LINE_A%%", "%Q%C" + pad_right(lines[0], max_len=36) + "%A") \
                       .replace("%%FEATURED_LINE_B%%", "%Q%C" + pad_right(lines[1], max_len=36) + "%A") \
                       .replace("%%FEATURED_LINE_C%%", "%Q%C" + pad_right(lines[2], max_len=36) + "%A")

    return body

if __name__ == "__main__":
    # CD to script directory
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )

    # Load json
    data = None
    with open("../data.json", "r") as f:
        data = json.load(f)["projects"]

    # Update timestamp
    out_path = "../docs/projects/index.html"
    with open("../src/projects/index.html", "r") as f:
        # Read file
        contents = f.read()

        # Create table of contents
        contents = contents.replace(
            "%%TABLE_OF_CONTENTS%%",
            "\n".join([indent(5) + f"<li><a href=\"#{y['year']}\">{y['year']}</a></li>" for y in data])
                [20:] # Remove extra leading whitespace w/ [20:]
        )

        # Load projects by year
        contents = contents.replace(
            "%%PROJECTS%%",
            "\n".join([gen_project_section(year, i == 0) for i, year in enumerate(data)])
                [12:] # Remove extra leading whitespace w/ [12:]
        )

        # Inject CSS
        contents = inject_inline_css(out_path, contents)

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", gen_timestamp(include_top_anchor=True))

        # Write to new file
        with open(out_path, "w") as f:
            f.write(contents)

    # Update shell page
    with open("../src/sh/projects.txt", "r") as f:
        # Read file
        contents = f.read()

        # Insert projects
        contents = gen_featured_project(data, contents)
        contents = gen_projects_table(data, contents)

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", pad_left(gen_timestamp_txt(), max_len=17))

        # Escape shell colors
        contents = escape_shell_colors(contents)

        # Write to new file
        with open("../docs/sh/projects.txt", "w") as f:
            f.write(contents + "\033[0m") # Clear ALL formatting