# Travis Heavener's Interactive Portfolio

Travis Heavener's official interactive web portfolio.

[wowtravis.com](https://wowtravis.com)

[![Build](https://github.com/travis-heavener/travis-heavener.github.io/actions/workflows/build.yml/badge.svg)](https://github.com/travis-heavener/travis-heavener.github.io/actions/workflows/build.yml)

## About
Travis Heavener (HEAVE-nur) is a fourth-year ITWS student at Rensselaer Polytechnic Institute. Travis often spends time outdoors and working on various programming projects. He is an amateur photographer, experienced developer, and avid PC enthusiast, applying his diverse range of skills wherever possible.

Connect with Travis on [LinkedIn](https://www.linkedin.com/in/travis-heavener/).

## Instructions

1. To build the website locally, you will need Python installed (see [python.org/downloads/](https://www.python.org/downloads/)).

2. Now that Python is installed, open a terminal window and navigate to the same directory as this README.md file (the root of the project).

3. Clone the site generator via `git clone https://github.com/travis-heavener/stylus.git generator`.

4. Run `python3 generator/src/main.py -vcf --config config.stylus.json` to build the website from the source (in the `src` directory) to the `public` directory.

5. To view the website, use an HTTP server like Apache or Nginx on this `public` directory.
