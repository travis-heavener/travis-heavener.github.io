import json
import os

from util import *

def gen_education_experience(data: any) -> str:
    s = indent(3) + """<div class="info-row">\n"""

    # Add each school
    for school in data:
        s += indent(4) + """<div class="info-div">\n"""

        # Add image
        img = school["img"]
        s += indent(5) + f"""<picture>\n""" \
            + indent(6) + f"""<source srcset="{img['srcset']}">\n""" \
            + indent(6) + f"""<img src="{img['default']}" fetchpriority="high" alt="{img['alt']}">\n""" \
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
                + indent(5) + f"""<title>{skill['name']}</title>\n""" \
                + indent(5) + f"""<use href="{skill['href']}"></use>\n""" \
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

def split_edu_exp_desc(desc: str) -> str:
    i = desc.find("<br>")
    format = lambda s: s.replace("&mdash;", "—").replace("&ndash;", "–")
    return (format(desc[:i]), format(desc[i+4:]))

if __name__ == "__main__":
    # CD to script directory
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )

    # Load json
    data = None
    with open("../data.json", "r") as f:
        data = json.load(f)["resume"]

    # Update timestamp
    out_path = "../docs/resume/index.html"
    with open("../src/resume/index.html", "r") as f:
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

        # Inject CSS
        contents = inject_inline_css(out_path, contents)

        # Replace header & timestamp
        contents = inject_header(contents)
        contents = contents.replace("%%TIMESTAMP%%", gen_timestamp(include_top_anchor=True))

        # Write to new file
        with open(out_path, "w") as f:
            f.write(contents)
    
    # Update shell page
    with open("../src/sh/resume.txt", "r") as f:
        # Read file
        contents = f.read()

        # Replace skills
        for i, exp in enumerate(data["skills"]):
            if i >= 12: break # Only use the first 12 skills
            letter = bytes([65 + i]).decode("utf-8")
            contents = contents.replace(f"%%SKILLS_{letter}%%", pad_right(exp["name"], max_len=12))

        # Replace education
        for i, exp in enumerate(data["education"]):
            letter = bytes([65 + i]).decode("utf-8")
            span, desc = split_edu_exp_desc(exp["desc"])
            contents = contents.replace(f"%%SCHOOL_TITLE_{letter}%%", pad_right(exp["name"], max_len=36))
            contents = contents.replace(f"%%SCHOOL_SPAN_{letter}%%", pad_right(span, max_len=36))
            contents = contents.replace(f"%%SCHOOL_DESC_{letter}%%", pad_right(desc, max_len=36))

        # Replace experience
        for i, exp in enumerate(data["experience"]):
            letter = bytes([65 + i]).decode("utf-8")
            span, desc = split_edu_exp_desc(exp["desc"])
            contents = contents.replace(f"%%EXPERIENCE_TITLE_{letter}%%", pad_right(exp["name"], max_len=36))
            contents = contents.replace(f"%%EXPERIENCE_SPAN_{letter}%%", pad_right(span, max_len=36))
            contents = contents.replace(f"%%EXPERIENCE_DESC_{letter}%%", pad_right(desc, max_len=36))

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", pad_left(gen_timestamp_txt(), max_len=17))

        # Escape shell colors
        contents = escape_shell_colors(contents)

        # Write to new file
        with open("../docs/sh/resume.txt", "w") as f:
            f.write(contents + "\033[0m") # Clear ALL formatting
    
    print("✅ Resume")