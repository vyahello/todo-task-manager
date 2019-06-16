# Todo task master
A simple todo task application written in _flask_ python micro-web framework.

[![Build Status](https://travis-ci.org/vyahello/todo-task-manager.svg?branch=master)](https://travis-ci.org/vyahello/todo-task-manager)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/todo-task-manager/badge.svg?branch=master)](https://coveralls.io/github/vyahello/todo-task-manager?branch=master)

# Run application
Run script from the root directory of the project:
```bash
python todo.py
```

# Run static code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, `pydocstyle` and `unittests` accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```
Anyway, this script is triggered via `Travis CI` .

# Contributing

- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
- `pip install -r requirements` to install all project dependencies
