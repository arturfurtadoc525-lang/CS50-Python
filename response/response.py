import validators
import sys


def main():
    print(validateEmail(input("What's your email address? ")))


def validateEmail(s):
        if validators.email(s):
            return "Valid"
        else:
            return "Invalid"


if __name__ == "__main__":
    main()
