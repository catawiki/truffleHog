from __future__ import print_function
import sys
from truffleHog.main import main as truffleHog_main


def main():
    try:
        truffleHog_main()
        return 0
    except SystemExit as error:
        return error.code


if __name__ == '__main__':
    sys.exit(main())