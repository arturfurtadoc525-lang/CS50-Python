import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    check = (
        r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/(.+?)".*?></iframe>'
    )
    if match := re.search(check, s):
        return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()
