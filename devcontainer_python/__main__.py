#!/usr/bin/env python3

from . import PACKAGE_NAME, PACKAGE_VERSION
from .utils import square


def main() -> None:
    print(f"Hello from {PACKAGE_NAME} version {PACKAGE_VERSION}!")
    print("3 squared is:", square(3))


if __name__ == "__main__":
    main()
