import json
import os

from util import *

if __name__ == "__main__":
    # CD to script directory
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )

    # Load json
    data = None
    with open("../data.json", "r") as f:
        data = json.load(f)["bio"]

    # Update timestamp
    with open("../templates/bio/index.html", "r") as f:
        # Read file
        contents = f.read()

        # Load paragraphs
        contents = contents.replace("%%PARAGRAPH 1.1%%", data["paragraphs"][0][0])
        contents = contents.replace("%%PARAGRAPH 1.2%%", data["paragraphs"][0][1])
        contents = contents.replace("%%PARAGRAPH 2.1%%", data["paragraphs"][1][0])
        contents = contents.replace("%%PARAGRAPH 2.2%%", data["paragraphs"][1][1])

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", gen_timestamp(include_top_anchor=True))

        # Write to new file
        with open("../docs/bio/index.html", "w") as f:
            f.write(contents)

    # Update shell page
    with open("../templates/sh/bio.txt", "r") as f:
        # Read file
        contents = f.read()

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", pad_left(gen_timestamp_txt(), max_len=17))

        # Escape shell colors
        contents = escape_shell_colors(contents)

        # Write to new file
        with open("../docs/sh/bio.txt", "w") as f:
            f.write(contents)