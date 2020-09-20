[![Build Status](https://travis-ci.org/vyahello/todo-task-manager.svg?branch=master)](https://travis-ci.org/vyahello/todo-task-manager)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/todo-task-manager/badge.svg?branch=master)](https://coveralls.io/github/vyahello/todo-task-manager?branch=master)
[![Issues](https://img.shields.io/github/issues/vyahello/todo-task-manager)](https://github.com/vyahello/todo-task-manager/issues)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE.md)
[![Hits-of-Code](https://hitsofcode.com/github/vyahello/todo-task-manager)](https://hitsofcode.com/view/github/vyahello/todo-task-manager)

# Todo task master
A simple todo task application written in [_flask_](http://flask.palletsprojects.com) python micro-web framework. 
Please use following link to observe how it looks: https://todo-task-master.herokuapp.com

**Tools**
- `python 3.6`
- `flask`
- `html5/css`
- `pytest`
- `shell`
- `travis/github CI`
- `heroku`

## Table of contents
- [Run application](#run-application)
- [Demo](#demo)
- [Run static code analysis](#run-static-code-analysis)
- [Deployment on heroku](#deployment-on-heroku)
- [Contributing](#contributing)

## Run application
Run script from the root directory of the project:
```bash
python todo.py
```

## Demo
**Home Page**
![Screenshot](static/home%20page.png)

**Update Task Page**
![Screenshot](static/update%20task.png)

## Run static code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, `pydocstyle` and `unittests` accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```
Anyway, this script is triggered via `Travis CI` and `GitHub CI`.

## Deployment on heroku
- Install heroku following by: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
- Login to heroku
```bash
heroku login
```
- Create an application
```bash
heroku create todo-task-master
```
- Commit and push repo into a heroku
```bash
git add . && git commit -m "My first heroku app" && git push heroku master
```
- Check heroku logs
```bash
heroku logs --tail
```
- Open an application via browser: https://todo-task-master.herokuapp.com

## Release notes

* 0.1.1
    * Enhance documentation
* 0.1.0
    * Introduce initial app version

## Meta
Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

## Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development dependencies
