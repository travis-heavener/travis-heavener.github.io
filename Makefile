SHELL := /bin/bash

.PHONY: all init clean

all:
	@make clean --no-print-directory
	@cp -r "src/." "docs/"

	@python3 ./tools/generate-home.py
	@python3 ./tools/generate-resume.py
	@python3 ./tools/generate-projects.py
	@python3 ./tools/generate-bio.py
	@python3 ./tools/generate-sitemap.py

	@chmod +x ./tools/minify.sh && ./tools/minify.sh
	@chmod +x ./tools/fetch_robots_txt.sh && ./tools/fetch_robots_txt.sh

init:
	@sudo apt install terser html-minifier-terser cleancss -y 1> /dev/null

clean:
	@if [ -d "docs" ]; then \
		rm -rf "docs"; \
	fi
	@mkdir "docs"