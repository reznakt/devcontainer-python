# devcontainer-python

This repository provides a template for setting up a Python development environment using devcontainers. It includes configurations for various tools and libraries commonly used in Python development.

## Toolchain

- [poetry](https://python-poetry.org/) - dependency management and packaging
- [ruff](https://docs.astral.sh/ruff/) - fast Python linter and code formatter
- [pyright](https://github.com/microsoft/pyright) - static type checker for Python (usually better than mypy)
- [vermin](https://pypi.org/project/vermin/) - checks whether your code is compatible with a given Python version
- [licensecheck](https://pypi.org/project/licensecheck/) - checks the compatibility of your dependencies' licenses with your project license
- [pre-commit](https://pre-commit.com/) - pre-commit hooks for linting, formatting, and other checks
- [poethepoet](https://poethepoet.natn.io/) - task management

## Getting Started

1. Create a new repository using this template.
2. Clone your new repository.
3. Open the repository in Visual Studio Code.
4. If prompted, reopen the repository in a devcontainer; otherwise, use the command palette (<kbd>Ctrl+Shift+P</kbd> or <kbd>Cmd+Shift+P</kbd>) and select "Reopen in Container".
5. Wait for the devcontainer to build and start.
6. Once the devcontainer is running, open the terminal and run the following command to install the dependencies:
   ```bash
   poetry install
   ```
7. To test whether everything is working correctly, run:
   ```bash
   poe start
   ```
   This command will run the example script provided in the `devcontainer_python` directory.
8. Don't forget to replace dummy values with your actual project values in `pyproject.toml` and other configuration files.
