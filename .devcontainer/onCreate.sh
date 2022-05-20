#!/bin/bash
set -euo pipefail

python -m pip install --upgrade pip

export PIPENV_VENV_IN_PROJECT=1
pipenv install -e .[dev]
