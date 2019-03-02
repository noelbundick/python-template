# Azure Python Boilerplate

[![Build Status](https://dev.azure.com/noelbundick/noelbundick/_apis/build/status/noelbundick.azure-python-boilerplate?branchName=master)](https://dev.azure.com/noelbundick/noelbundick/_build/latest?definitionId=38&branchName=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


Some scaffolding and structure to help bootstrap Python projects on Azure

## One-time setup

```shell
# Create a virtual environment and activate it
python3 -m venv .venv
source .venv/bin/activate

# Install boilerplate in editable mode with dev dependencies
python -m pip install '.[dev]'
```

## Developing in [Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

* Open VS Code, everything's all wired up!
* Hit `F5` to start debugging
* Hit `Ctrl+F5` to start w/o debugging
* Hit `Ctrl+Shift+P`/`Cmd+Shift+P`
  * `Tasks: Run Task` -> `boilerplate CLI` to run boilerplate as a VS Code task w/ specified args
  * `Python: Run All Unit Tests` to run tests via pytest

> You may need to open a `.py` file to activate the Python VS Code extension


## Developing in a terminal

```shell
# Make sure your virtual environment is active
source .venv/bin/activate

# running with console_script
boilerplate foo

# running as a module
python -m boilerplate bar

# running tests
pytest
tox
```