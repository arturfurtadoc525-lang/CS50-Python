import sys
from PIL import Image, ImageOps
from pathlib import Path


def main():

    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif not Path(sys.argv[1]).suffix == Path(sys.argv[2]).suffix:
            sys.exit("Input and output have different extensions")
        for _ in sys.argv[1:]:
            if not ".jpg" in _ and not ".jpeg" in _ and not ".png" in _:
                sys.exit("Not a Image file")
        imgBefore = sys.argv[1]
        imgAfter = sys.argv[2]
        with Image.open(imgBefore) as before:
            with Image.open("shirt.png") as shirt:
                edit = ImageOps.fit(before, shirt.size)
                edit.paste(shirt, shirt)

                edit.save(imgAfter)

    except FileNotFoundError:
        sys.exit("File does not exist")


main()
