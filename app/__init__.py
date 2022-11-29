"""app"""

import os

from app._env import env
from app.log import log

os.environ["TZ"] = "UTC"

__version__ = "0.0.0"
__all__ = ["__version__", "log", "env"]
