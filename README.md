# Azure Python Boilerplate

Some scaffolding and structure to help bootstrap Python projects on Azure

## VS Code development

One-time setup

```shell
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies for dev & testing
python -m pip install -r ./requirements.dev.txt
```

Day-to-day development

* Open VS Code, everything's all wired up!
* Hit `F5` to start debugging
* Hit `Ctrl+F5` to start w/o debugging
* Hit `Ctrl+Shift+P`/`Cmd+Shift+P` -> `Tasks: Run Task` -> `boilerplate CLI` to run boilerplate as a VS Code task w/ specified args


## Console development

One-time setup

```shell
# Create a virtual environment and activate it
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies for dev & testing
python -m pip install -r ./requirements.dev.txt

# Install module in editable mode
python setup.py develop
```

Day-to-day development

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