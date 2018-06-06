import logging
import sys

from . import shellcheck
from . import sc2006
from . import sc2016
from . import sc2034
from . import sc2035
from . import sc2046
from . import sc2086
from . import sc2155
from . import sc2181


def fix_all(path: str):
    fixers = [sc2006, sc2016, sc2034, sc2035, sc2046, sc2086, sc2155, sc2181]
    for fixer in fixers:
        try:
            fixer.fix(path)
        except Exception as e:
            logging.error(e)
