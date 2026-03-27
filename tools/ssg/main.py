#!/usr/bin/env python3

"""

Author: Travis Heavener
Date: March 26, 2026

Steps:
    1. Copy source
    2. Build the site from the HTML skeleton
    3. Build sitemap.xml
    4. Run accessibility audit on HTML
    5. Minify HTML/CSS/JS
    6. Fetch robots.txt

"""

import os
from pathlib import Path
from time import time
import traceback

from auditor import audit_html
from injector import inject_html
from tools import *

if __name__ == "__main__":
    # Debug profiling
    start = time()

    # Update CWD to project directory
    os.chdir( Path(__file__).resolve().parent.parent.parent )

    try:
        # 1. Copy source
        updated_files = copy_source()

        # 2. Build site from HTML skeleton
        inject_html(updated_files)

        # 3. Build sitemap.xml
        html_files = tuple( [str(p) for p in Path(DEST_PATH).rglob("*.html")] )
        build_sitemap(html_files)

        # 4. Run accessibility audit
        audit_html(html_files)

        # 5. Minify assets
        if not isarg("x"):
            minify()
        else:
            warn("Skipping minification")

        # 6. Fetch robots.txt
        fetch_robots()

        # Log success
        log(f"Build success ({round(time() - start)}s).")
    except Exception as e:
        log(f"Build failed ({round(time() - start)}s):")
        traceback.print_exc()
