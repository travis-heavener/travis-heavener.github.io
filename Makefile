SHELL := /bin/bash

.PHONY: init clean

TARGETS := $(shell find ./src -type f | tr '\n' ' ')

all: ./public/CNAME

./public/CNAME: $(TARGETS)
	@make clean --no-print-directory
	@cp -r "src/." "public/"

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
	@if [ -d "public" ]; then \
		rm -rf "public"; \
	fi
	@mkdir "public"