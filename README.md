# Todo task master
A simple todo task application written in [_flask_](http://flask.palletsprojects.com) python micro-web framework. 
Please use following link to observe how it looks: https://todo-task-master.herokuapp.com

[![Build Status](https://travis-ci.org/vyahello/todo-task-manager.svg?branch=master)](https://travis-ci.org/vyahello/todo-task-manager)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/todo-task-manager/badge.svg?branch=master)](https://coveralls.io/github/vyahello/todo-task-manager?branch=master)

## Table of contents
- [Run application](#run-application)
- [Demo](#demo)
- [Run static code analysis](#run-static-code-analysis)
- [Deployment on heroku](#deployment-on-heroku)
- [Contributing](#contributing)

# Run application
Run script from the root directory of the project:
```bash
python todo.py
```

# Demo
Home Page
![Screenshot](static/home%20page.png)

Update Task Page
![Screenshot](static/update%20task.png)

# Run static code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, `pydocstyle` and `unittests` accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```
Anyway, this script is triggered via `Travis CI` and `GitHub CI`.

Sample output from _static code analysis_ tool:
```bash
tests/test_applications.py::test_route_from_str[root-/] PASSED                                                                                                                                     [  4%]
tests/test_applications.py::test_route_from_str[home_page-/index.html] PASSED                                                                                                                      [  9%]
tests/test_applications.py::test_route_from_str[delete_id-/delete/<int:identity>] PASSED                                                                                                           [ 13%]
tests/test_applications.py::test_route_from_str[update_id-/update/<int:identity>] PASSED                                                                                                           [ 18%]
tests/test_applications.py::test_route_from_str[update_page-/update.html] PASSED                                                                                                                   [ 22%]
tests/test_applications.py::test_wrong_route_from_str PASSED                                                                                                                                       [ 27%]
tests/test_applications.py::test_allowed_routes PASSED                                                                                                                                             [ 31%]
tests/test_applications.py::test_wrong_route PASSED                                                                                                                                                [ 36%]
tests/test_applications.py::test_str_route PASSED                                                                                                                                                  [ 40%]
tests/test_applications.py::test_call_custom PASSED                                                                                                                                                [ 45%]
tests/test_applications.py::test_call_todo PASSED                                                                                                                                                  [ 50%]
tests/test_applications.py::test_todo_setup_module PASSED                                                                                                                                          [ 54%]
tests/test_applications.py::test_todo_setup_database PASSED                                                                                                                                        [ 59%]
tests/test_applications.py::test_todo_setup_static PASSED                                                                                                                                          [ 63%]
tests/test_applications.py::test_todo_setup_templates PASSED                                                                                                                                       [ 68%]
tests/web/test_api.py::test_number_of_methods PASSED                                                                                                                                               [ 72%]
tests/web/test_api.py::test_index_methods_number PASSED                                                                                                                                            [ 77%]
tests/web/test_api.py::test_delete_methods_number PASSED                                                                                                                                           [ 81%]
tests/web/test_api.py::test_method[POST-POST] PASSED                                                                                                                                               [ 86%]
tests/web/test_api.py::test_method[GET-GET] PASSED                                                                                                                                                 [ 90%]
tests/web/test_api.py::test_method[PUT-PUT] PASSED                                                                                                                                                 [ 95%]
tests/web/test_api.py::test_method[DELETE-DELETE] PASSED                                                                                                                                           [100%]

---------- coverage: platform darwin, python 3.6.5-final-0 -----------
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
lib/__init__.py           7      0   100%
lib/applications.py      58      5    91%   64, 69, 74, 86, 107
lib/databases.py         34      3    91%   53, 57, 61
lib/models.py             8      1    88%   15
lib/routes.py            27     14    48%   15-19, 25-27, 33-38
lib/web/__init__.py       0      0   100%
lib/web/api.py           15      1    93%   26
---------------------------------------------------
TOTAL                   149     24    84%


======================================================================================= 22 passed in 0.89 seconds ========================================================================================

Running pylint analysis ...
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

Running mypy analysis ...
Running flake8 analysis ...
0
Running black analysis ...
All done! ✨ 🍰 ✨
12 files would be left unchanged.
Running pydocstyle analysis ...
0
Removing code analysis trash if present ...
pytest trash is removed
mypy trash is removed
Code analysis is passed
```

# Deployment on heroku
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


# Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
- `pip install -r requirements` to install all project dependencies
