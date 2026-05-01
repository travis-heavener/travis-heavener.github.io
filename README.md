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

3. Clone the site generator via `git clone https://github.com/travis-heavener/stylus.git generator`.

4. Run `python3 generator/src/main.py -vcf --config config.stylus.json` to build the website from the source (in the `src` directory) to the `public` directory.

5. To view the website, use an HTTP server like Apache or Nginx on this `public` directory.
