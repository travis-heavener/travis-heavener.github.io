import json
import os

from util import *

if __name__ == "__main__":
    # CD to script directory
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )

    # Update timestamp
    with open("../templates/bio/index.html", "r") as f:
        # Read file
        contents = f.read()

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", gen_timestamp(include_top_anchor=True))

        # Write to new file
        with open("../web/bio/index.html", "w") as f:
            f.write(contents)