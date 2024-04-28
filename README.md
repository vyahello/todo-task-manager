![Screenshot](logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/todo-task-manager.svg?branch=master)](https://travis-ci.org/vyahello/todo-task-manager)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/todo-task-manager/badge.svg?branch=master)](https://coveralls.io/github/vyahello/todo-task-manager?branch=master)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE.md)

# Todo task master
A simple todo task application written in [flask](http://flask.palletsprojects.com) python micro-web framework. 

![Screenshot](static/home%20page.png)

![Screenshot](static/update%20task.png)

## Tools

### Production

- python 3.7
- [flask](http://flask.palletsprojects.com)
- html5/css
- shell
- [heroku](https://todo-task-master.herokuapp.com)

### Development

- [travis](https://travis-ci.org/) CI
- [pytest](https://pypi.org/project/pytest/) framework
- [black](https://black.readthedocs.io/en/stable/) code formatter
- [mypy](http://mypy.readthedocs.io/en/latest) static tyler
- [pylint](https://www.pylint.org/) code style
- [flake8](http://flake8.pycqa.org/en/latest/) code formatter


## Quick start
Run script from the root directory of the project:
```bash
git clone git@github.com:vyahello/todo-task-manager.git
pip install -r requirements.txt
python todo.py
```

## Development notes

### Run static code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, `pydocstyle` and `unittests` accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```
Anyway, this script is triggered via `Travis CI` and `GitHub CI`.

## Deployment on heroku

Please check [deployment](DEPLOYMENT.md) file for app deployment.

## Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

## Meta
Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `Apache 2.0` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

## Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request

