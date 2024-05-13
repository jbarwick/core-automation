import sys
from core_automation import run_local

def main():
    run_local(sys.argv[1:])

if __name__ == "__main__":
    main()