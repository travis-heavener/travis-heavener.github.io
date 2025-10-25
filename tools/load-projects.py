import json
import os

from util import *

if __name__ == "__main__":
    # CD to script directory
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )

    # Load json
    data = None
    with open("../data.json", "r") as f:
        data = json.load(f)["projects"]

    print(data)

    # Update timestamp
    with open("../templates/projects/index.html", "r") as f:
        # Read file
        contents = f.read()

        # Create table of contents
        contents = contents.replace(
            "%%TABLE_OF_CONTENTS%%",
            (" " * 20 + "\n").join([f"<li><a href=\"#{y['year']}\">{y['year']}</a></li>" for y in data])
        )

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", gen_timestamp(include_top_anchor=True))

        # Write to new file
        with open("../web/projects/index.html", "w") as f:
            f.write(contents)