from datetime import datetime, timezone
import os

from util import *

def get_mod_ts(path: str) -> str:
    mtime = os.path.getmtime(path)
    dt = datetime.fromtimestamp(mtime, tz=timezone.utc).replace(microsecond=0)
    return dt.isoformat()

if __name__ == "__main__":
    # CD to script directory
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )

    # Update timestamp
    with open("../templates/sitemap.xml", "r") as f:
        # Read file
        contents = f.read()

        # Load paragraphs
        contents = contents.replace("%%HOME_LASTMOD%%", get_mod_ts("../templates/index.html"))
        contents = contents.replace("%%RESUME_LASTMOD%%", get_mod_ts("../templates/resume/index.html"))
        contents = contents.replace("%%PROJECTS_LASTMOD%%", get_mod_ts("../templates/projects/index.html"))
        contents = contents.replace("%%BIO_LASTMOD%%", get_mod_ts("../templates/bio/index.html"))

        # Write to new file
        with open("../docs/sitemap.xml", "w") as f:
            f.write(contents)