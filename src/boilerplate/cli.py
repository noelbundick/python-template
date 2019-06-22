import sys
from boilerplate import Hello


def main():
    args = sys.argv[1:]

    hello = Hello()
    message = hello.greet(*args)
    print(message)
