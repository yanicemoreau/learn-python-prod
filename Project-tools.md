# Project tools

This file summarize diferent tools that are useful in a python project: how they work and what they do

## Writing clean code

This section enumerates some tools to make code cleaner, easier to read to increase it's maintainability and keep up with best practices

### Black: code formatting

Black is a tool that formats code based on some rules. It covers issues such as spacing and line breaks. An interesting functionality to have with it is to activate it on save of file. It can be parametrized on VSCode's config file.

### Pylint: code linter

Pylint is a linter for python, with different levels of messages. It can be integrated with VSCode. Some warnings can be disabled by comments in the code, parametrization through VSCode's config or a separated config file named __.pylintrc__. An interesting functionality to have with it is to activate it on save of file.

Similar tool : flake8

### Isort: imports sorter

### Mypy: Type checking

Mypy is a tool that hilights typing error when using Python's static typing. It is integrated in VSCode's python extension and can be enabled by adding this in the __settings.json__ file: ```"python.linting.mypyEnabled": true```

## Code quality

### Radon : code metrics

Similar tools : mccabe, xenon


## Logging

### Datadog : log viewer
 