import json
import os

from util import *

if __name__ == "__main__":
    # CD to script directory
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )

    # Update timestamp
    with open("../src/index.html", "r") as f:
        # Read file
        contents = f.read()

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", gen_timestamp(include_top_anchor=False))

        # Write to new file
        with open("../docs/index.html", "w") as f:
            f.write(contents)

    # Update shell page
    with open("../src/sh/index.txt", "r") as f:
        # Read file
        contents = f.read()

        # Replace timestamp
        contents = contents.replace("%%TIMESTAMP%%", pad_left(gen_timestamp_txt(), max_len=17))

        # Escape shell colors
        contents = escape_shell_colors(contents)

        # Write to new file
        with open("../docs/sh/index.txt", "w") as f:
            f.write(contents + "\033[0m") # Clear ALL formatting