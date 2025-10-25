SHELL := /bin/bash

all: clean init_copy home resume projects bio

.PHONY: clean init_copy

init_copy:
	@cp -r "templates/." "web/"

clean:
	@if [ -d "web" ]; then \
		rm -rf "web"; \
	fi
	@mkdir "web"

home:
	@echo "TODO - HOME"

resume:
	@echo "TODO - RESUME"

projects:
	@echo "TODO - PROJECTS"

bio:
	@echo "TODO - BIO"