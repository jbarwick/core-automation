import sys
from .run_local import run_local
from .run_remote import run_remote

def main():
    run_local(sys.argv[1:])
    run_remote(sys.argv[1:])
    