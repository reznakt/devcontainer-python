import importlib.metadata
from typing import Final


PACKAGE_NAME: Final = __name__
PACKAGE_VERSION: Final = importlib.metadata.version(PACKAGE_NAME)
