import json
import os

from util import *

def indent(n: int) -> str:
    return " " * (4 * n)

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
                s += indent(6) + f"""<img class="project-img" loading="{img['loading']}" src="{img['src']}" alt="{img['alt']}">\n"""

            s += indent(5) + """</div>\n"""
        else:
            img = project["imgs"][0]
            s += indent(5) + f"""<img class="project-img" loading="{img['loading']}" src="{img['src']}" alt="{img['alt']}">\n"""

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

if __name__ == "__main__":
    # CD to script directory
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )

    # Load json
    data = None
    with open("../data.json", "r") as f:
        data = json.load(f)["projects"]

    # Update timestamp
    with open("../templates/projects/index.html", "r") as f:
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

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", gen_timestamp(include_top_anchor=True))

        # Write to new file
        with open("../web/projects/index.html", "w") as f:
            f.write(contents)