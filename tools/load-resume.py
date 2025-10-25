import json
import os

from util import *

def indent(n: int) -> str:
    return " " * (4 * n)

def gen_education_experience(data: any) -> str:
    s = indent(3) + """<div class="info-row">\n"""

    # Add each school
    for school in data:
        s += indent(4) + """<div class="info-div">\n"""

        # Add image
        img = school["img"]
        s += indent(5) + f"""<picture>\n""" \
            + indent(6) + f"""<source srcset="{img['srcset']}">\n""" \
            + indent(6) + f"""<img src="{img['default']}" alt="{img['alt']}">\n""" \
            + indent(5) + "</picture>\n"

        # Add title & desc
        s += indent(5) + f"""<h3><a href="{school['href']}">{school['name']}</a></h3>\n"""
        s += indent(5) + f"""<p>{school['desc']}</p>\n"""

        s += indent(4) + """</div>\n"""

    # Close projects row
    s += indent(3) + """</div>\n"""

    return s[12:] # Remove extra leading whitespace w/ [12:]

def gen_skills_list(data: any) -> str:
    s = indent(3) + """<div id="skills-list">\n"""

    for skill in data:
        if ".svg" in skill["href"]:
            s += indent(4) + f"""<svg{'' if 'class' not in skill else f' class=\"{skill['class']}\"'}>\n""" \
                + indent(5) + f"""<use href="{skill['href']}"></use>\n""" \
                + indent(5) + f"""<title>{skill['name']}</title>\n""" \
                + indent(4) + "</svg>\n"
        else:
            s += indent(4) + f"""<img src="{skill['href']}" alt="{skill['alt']}">\n"""

    s += indent(3) + """</div>\n"""
    return s[12:] # Remove extra leading whitespace w/ [12:]

def gen_activities_accomplishments(data: any) -> str:
    s = ""
    for activity in data:
        s += indent(3) + f"""<div class="broken-text-fixed">\n""" \
            + indent(4) + f"""<p>{activity['title']}</p>\n""" \
            + indent(4) + f"""<p>{activity['duration']}</p>\n""" \
            + indent(3) + "</div>\n"
    return s[12:] # Remove extra leading whitespace w/ [12:]

if __name__ == "__main__":
    # CD to script directory
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )

    # Load json
    data = None
    with open("../data.json", "r") as f:
        data = json.load(f)["resume"]

    # Update timestamp
    with open("../templates/resume/index.html", "r") as f:
        # Read file
        contents = f.read()

        # Load education & experience
        contents = contents.replace("%%EDUCATION%%", gen_education_experience(data["education"]))
        contents = contents.replace("%%EXPERIENCE%%", gen_education_experience(data["experience"]))

        # Load skills list
        contents = contents.replace("%%SKILLS_LIST%%", gen_skills_list(data["skills"]))

        # Load activities & accomplishments
        contents = contents.replace("%%ACTIVITIES%%", gen_activities_accomplishments(data["activities"]))
        contents = contents.replace("%%ACCOMPLISHMENTS%%", gen_activities_accomplishments(data["accomplishments"]))

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", gen_timestamp(include_top_anchor=True))

        # Write to new file
        with open("../web/resume/index.html", "w") as f:
            f.write(contents)