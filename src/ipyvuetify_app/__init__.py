"""Prepare VuaApp to be directly importable"""
# Standard library imports

# Third party imports

# Local imports
from .app import VueApp
from .router_example import VueAppRouter

__all__ = ["VueApp", "VueAppRouter"]
