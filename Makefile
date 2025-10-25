SHELL := /bin/bash

all: clean init_copy home resume projects bio sitemap

.PHONY: clean init_copy home reusme projects bio sitemap

init_copy:
	@cp -r "templates/." "web/"

clean:
	@if [ -d "web" ]; then \
		rm -rf "web"; \
	fi
	@mkdir "web"

home:
	@python3 ./tools/load-home.py

resume:
	@python3 ./tools/load-resume.py

projects:
	@python3 ./tools/load-projects.py

bio:
	@python3 ./tools/load-bio.py

sitemap:
	@echo "TODO - SITEMAP"