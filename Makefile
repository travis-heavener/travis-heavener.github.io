SHELL := /bin/bash

all: clean init_copy robots_txt home resume projects bio sitemap minify

.PHONY: init clean init_copy robots_txt home resume projects bio sitemap minify

init:
	@sudo apt install terser html-minifier-terser cleancss -y 1> /dev/null

init_copy:
	@cp -r "src/." "docs/"
	@find docs -type f -name "*.css" -exec rm {} \;

robots_txt:
	@chmod +x ./tools/fetch_robots_txt.sh && ./tools/fetch_robots_txt.sh

clean:
	@if [ -d "docs" ]; then \
		rm -rf "docs"; \
	fi
	@mkdir "docs"

home:
	@python3 ./tools/generate-home.py
	@echo "✅ Home"

resume:
	@python3 ./tools/generate-resume.py
	@echo "✅ Resume"

projects:
	@python3 ./tools/generate-projects.py
	@echo "✅ Projects"

bio:
	@python3 ./tools/generate-bio.py
	@echo "✅ Bio"

sitemap:
	@python3 ./tools/generate-sitemap.py
	@echo "✅ Sitemap"

minify:
	@find ./docs/ -type f -name "*.js" -exec terser {} -o {} \;
	@find ./docs/ -type f -name "*.css" -exec cleancss -o {} {} \;
	@find ./docs/ -type f -name "*.html" -exec html-minifier-terser {} -o {} \
		--collapse-whitespace --remove-comments --minify-css --use-short-doctype \;