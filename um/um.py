import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    check = r"\bum\b"

    if mach := re.findall(check, s, re.IGNORECASE):
        return len(mach)


if __name__ == "__main__":
    main()
