#!/usr/bin/env python3

import argparse
import json
import os
import sys


def main(env_vars, quiet=False, pretty=False):
    temp_vars = {}

    if len(env_vars) == 0:
        for x in os.environ:
            temp_vars[x] = os.environ[x].split(";")
    else:
        for x in env_vars:
            if x in os.environ:
                temp_vars[x] = os.environ[x].split(";")
            else:
                if not quiet:
                    print(
                        f"ERROR: `{x}` is not a current environment variable",
                        file=sys.stderr,
                    )

    out = json.dumps(temp_vars, indent=4) if pretty else json.dumps(temp_vars)

    print(out)
    return


def get_args():
    parser = argparse.ArgumentParser(description="Print env variables sanely")
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Suppress error messages when environment variable not found",
    )
    parser.add_argument(
        "-p",
        "--pretty",
        action="store_true",
        help="Print vars with indentation",
    )
    parser.add_argument(
        "env_vars",
        nargs="*",
        help="Space separated list of environment variable to lookup",
    )
    return vars(parser.parse_args())


if __name__ == "__main__":
    args = get_args()
    main(**args)
