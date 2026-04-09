import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    check = r"^([1-9]|1[0-2])(:?[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(:?[0-5][0-9])? (AM|PM)$"
    if match := re.search(check, s, re.IGNORECASE):
        if match.group(3) == "AM":
            if match.group(1) == "12":
                start = "00"
            else:
                start = "0" + match.group(1)
        else:
            if match.group(1) == "12":
                start = "12"
            else:
                start = str(int(match.group(1)) + 12)
        if match.group(2) == None:
            start += ":00"
        else:
            start += match.group(2)
        if match.group(6) == "AM":
            if match.group(4) == "12":
                end = "00"
            else:
                end = "0" + match.group(4)
        else:
            if match.group(4) == "12":
                end = "12"
            else:
                end = str(int(match.group(4)) + 12)
        if match.group(5) == None:
            end += ":00"
        else:
            end += match.group(5)

        return f"{start} to {end}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
