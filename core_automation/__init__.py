import sys
from .run_local import run_local
from .run_remote import run_remote

def main():
    """
    This is the main entry point for the core_automation package.
    Called from core.py
    """
    run_local(sys.argv[1:])
    run_remote(sys.argv[1:])
