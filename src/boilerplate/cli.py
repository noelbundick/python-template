import sys
from boilerplate.hello import Hello


def main():
    args = sys.argv[1:]

    d = Hello()
    print(f"Hello, {d.Word(*args)}!")
