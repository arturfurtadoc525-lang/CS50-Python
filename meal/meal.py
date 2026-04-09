import string
import re

def main():
    time = input("What time is it? ")
    if re.search("am", time, re.IGNORECASE):
        if convert(time) < 12:
            print(f"breakfast time")
        else:
            print(f"lunch time")
    elif re.search("pm", time, re.IGNORECASE):
        if convert(time) < 6:
            print(f"lunch time")
        else:
            print(f"dinner time")
    else:
        if convert(time) < 12:
            print(f"breakfast time")
        elif convert(time) < 18:
            print(f"lunch time")
        else:
            print(f"dinner time")

def convert(time):

    time = time.lower()
    time = time.strip()
    time = time.replace("-", " ")

    limpar = str.maketrans("", "", string.punctuation)
    time = time.translate(limpar)

    if re.search("am", time, re.IGNORECASE):
        time = time[:-2]
    elif re.search("pm", time, re.IGNORECASE):
        time = time[:-2]

    h = int(time[:-2])
    min = int(time[-2:])
    time = h+(min/60)

    return time


if __name__ == "__main__":
    main()
