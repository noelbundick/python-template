""" Boilerplate CLI """

import sys
from boilerplate import Hello


def main():
    """CLI entrypoint"""
    args = sys.argv[1:]

    hello = Hello()
    message = hello.greet(*args)
    print(message)
