import sys

def main():
    i = 0
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) <= 1:
            sys.exit("Too few command-line arguments")
        elif not ".py" in sys.argv[1]:
            sys.exit("Not a Python file")
        selected = sys.argv[1]
        with open(selected) as file:
            for line in file:
                if line.lstrip(" ").startswith("#"):
                    ...
                elif not line.strip():
                    ...
                else:
                    i +=1

        print(i)

    except FileNotFoundError:
        sys.exit("File does not exist")

main()
