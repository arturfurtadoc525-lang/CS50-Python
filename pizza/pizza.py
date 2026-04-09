import sys
import csv
from tabulate import tabulate


def main():
    menu = []
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) <= 1:
            sys.exit("Too few command-line arguments")
        elif not ".csv" in sys.argv[1]:
            sys.exit("Not a CSV file")

        selected = sys.argv[1]
        with open(selected) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)

        print(tabulate(menu, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


main()
