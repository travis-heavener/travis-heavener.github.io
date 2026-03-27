# Travis Heavener's Interactive Portfolio

Travis Heavener's official interactive web portfolio.

[wowtravis.com](https://wowtravis.com)

[![Build](https://github.com/travis-heavener/travis-heavener.github.io/actions/workflows/build.yml/badge.svg)](https://github.com/travis-heavener/travis-heavener.github.io/actions/workflows/build.yml)

## About
Travis Heavener (HEAVE-nur) is currently a third year student at Rensselaer Polytechnic Institute majoring in IT & Web Science. In his spare time, Travis often works on independent programming projects or spends his time with friends. Travis is a modest car enthusiast and a longtime swimmer, with a passion for full stack and collaborative project development.

From [LinkedIn](https://www.linkedin.com/in/travis-heavener/):

> I'm a third-year student at Rensselaer Polytechnic Institute studying IT & Web Science, with a strong interest in building performant, scalable software systems. I've been programming since age twelve and have pursued both academic and independent projects across full-stack development, server programming, and systems engineering.
> 
> I'm the developer of Mercury, a cross-platform, RFC-compliant HTTP server written in C++, and BinGo, a gamified Android application built with React Native that encourages physical activity through reward-driven progression. While my primary focus is web and backend development, I actively seek out low-level and systems-oriented projects to broaden my skill set.
> 
> Beyond software development, I've gained professional experience through IT internships with Next Phase Solutions and Services in 2023 and 2025, where I worked with cloud infrastructure, networking, and cybersecurity. Earlier roles in customer-facing environments helped shape my communication, leadership, and problem-solving skills.
> 
> Outside of work, I'm a longtime swimmer, amateur photographer, and computer enthusiast who enjoys learning by building.

## Instructions

1. To build the website locally, you will need Python installed (see [python.org/downloads/](https://www.python.org/downloads/)).

2. Now that Python is installed, open a terminal window and navigate to the same directory as this README.md file (the root of the project).

3. Run `python3 generator/main.py` to build the website from the source (in the `src` directory) to the `public` directory.

4. To view the website, use an HTTP server like Apache or Nginx on this `public` directory.

### Generator Script Options

The `generator/main.py` Python script has a few command-line arguments that it can be passed:

| Argument | Usage                          | Description                                                                                   |
|----------|--------------------------------|-----------------------------------------------------------------------------------------------|
| -f       | `python3 generator/main.py -f` | Copy all files freshly from `src` to `public` instead of only ones modified since last build. |
| -v       | `python3 generator/main.py -v` | Prints additional debug info to the terminal.                                                 |
| -c       | `python3 generator/main.py -c` | Uses color for printing information to the terminal.                                          |
| -x       | `python3 generator/main.py -x` | Skips minification for all assets.                                                            |

Note: to use multiple arguments, combine them (ex: `-vcf` will print verbose logs with colored output and force-rebuilds all assets)

## Special URLs
The following URLs will redirect you to where you need to go ;)

| Name      | URL                                                            |
|-----------|----------------------------------------------------------------|
| LinkedIn  | [wowtravis.com/my/linkedin](https://wowtravis.com/my/linkedin) |
| GitHub    | [wowtravis.com/my/github](https://wowtravis.com/my/github)     |
| This Repo | [wowtravis.com/this](https://wowtravis.com/this)               |

## Credits

This portfolio is made possible by the following sources:

- `robots.txt` is automatically fetched from https://github.com/ai-robots-txt/ai.robots.txt (see [licenses/ai_robots_txt_LICENSE.txt](licenses/ai_robots_txt_LICENSE.txt)).