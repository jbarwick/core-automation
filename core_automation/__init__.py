import sys
from .run_local import run_local
from .util import main_util, other_util

__all__ = ["run_local", "main_util", "other_util"]

def main():
    run_local(sys.argv[1:])