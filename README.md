# Python Project Template

![Build](https://github.com/noelbundick/python-template/actions/workflows/build.yaml/badge.svg)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


Some scaffolding and structure to help bootstrap Python package projects

## Getting started

* [Use this template](https://github.com/noelbundick/python-template/generate) to create a new repo
* Create a new [Codespace](https://docs.github.com/en/codespaces/getting-started/quickstart)

## Developing in [Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

* Open VS Code, everything's all wired up!
* Hit `F5` to start debugging
* Hit `Ctrl+F5` to start w/o debugging
* Hit `Ctrl+Shift+P`/`Cmd+Shift+P`
  * `Tasks: Run Task` -> `boilerplate CLI` to run boilerplate as a VS Code task w/ specified args
  * `Test: Run All Tests` to run tests via pytest

## Developing in a terminal

```shell
# running with console_script
boilerplate foo

# running as a module
python -m boilerplate bar

# linting
pylint src
flake8

# tests
pytest

# check for security issues
pipenv check

# update packages
pipenv update

# build a package
python -m build
```
