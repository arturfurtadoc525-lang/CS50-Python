import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    check = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    if check:
        for _ in range(1, 5):
            if int(check.group(_)) > 255 or (len(check.group(_)) > 1 and check.group(_).startswith("0")):
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
