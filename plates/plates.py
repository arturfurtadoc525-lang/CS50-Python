import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def special(s):
    pattern = re.compile(r"[^a-zA-Z0-9\s]")
    return bool(pattern.search(s))


def is_valid(s):
    if not (len(s) <= 6 and len(s) >= 2):
        return False

    if special(s):
        return False

    if s[0:1].isdigit():
        return False

    n = False
    for i in range(len(s)):
        if s[i].isdigit():
            if n == False and s[i] == "0":
                return False
            n = True
        if not s[i].isdigit() and n == True:
            return False
    return True


main()
