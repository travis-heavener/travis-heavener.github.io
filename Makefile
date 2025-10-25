SHELL := /bin/bash

all: clean init_copy home resume projects bio sitemap

.PHONY: clean init_copy home reusme projects bio sitemap

init_copy:
	@cp -r "templates/." "docs/"

clean:
	@if [ -d "docs" ]; then \
		rm -rf "docs"; \
	fi
	@mkdir "docs"

home:
	@python3 ./tools/load-home.py
	@echo "✅ Home"

resume:
	@python3 ./tools/load-resume.py
	@echo "✅ Resume"

projects:
	@python3 ./tools/load-projects.py
	@echo "✅ Projects"

bio:
	@python3 ./tools/load-bio.py
	@echo "✅ Bio"

sitemap:
	@python3 ./tools/load-sitemap.py
	@echo "✅ Sitemap"