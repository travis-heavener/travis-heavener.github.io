SHELL := /bin/bash

all: clean init_copy robots_txt home resume projects bio sitemap

.PHONY: clean init_copy home resume projects bio sitemap

init_copy:
	@cp -r "templates/." "docs/"

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