# Cal Poly Electrical Engineering Department Equipment VISA libraries

By: Dominic Gaiero

This library is designed to interface with all standard lab equipment
on the lab benches.

* [Cal Poly Electrical Engineering Department Equipment VISA libraries](#cal-poly-electrical-engineering-department-equipment-visa-libraries)
  * [Installation](#installation)
  * [Development](#development)
  * [Documentation](#documentation)

## Installation

**TODO** -> Need to package for easy installation

1. Install all necessary dependencies from `requirements.txt`
2. Use library

## Development

1. Create and activate a virtural environment: `python -m venv env`
2. `env/Activate.bat`
3. `pip install -U requirements.txt`
4. Development is done on development branch.

## Documentation

This project is auto-documented from the docstrings in each file. Follow guidelines for `reStructured Text`. To build the documentation:
1. `cd docs`
2. `make.bat html`: please note, right now, this only works on windows platforms. You can also make a LaTeX document and then generate a PDF file.

The documentation is in a different repository ([cpee-visa-docs](https://github.com/dgaiero/cpee-VISA-docs))

You can view the documentation at: [https://about.dgaiero.me/cpee-visa-docs/](https://about.dgaiero.me/cpee-visa-docs/)