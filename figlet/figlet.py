import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


def main():
    listFont = figlet.getFonts()
    if len(sys.argv) == 1:
        font = random.choice(listFont)
        figlet.setFont(font=font)
    elif len(sys.argv) == 3:
        flag = sys.argv[1]
        font = sys.argv[2]
        if flag not in ["-f", "--font"] or font not in listFont:
            sys.exit(1)
        else:
            figlet.setFont(font=font)
    else:
        sys.exit(1)

    response = input("Input: ")
    print(f"Output: \n" + figlet.renderText(response))
    sys.exit(0)


main()
