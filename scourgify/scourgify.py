import sys
import csv


def main():
    lname = []
    lsurname = []
    lhouse = []
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        for _ in sys.argv:
            if not ".csv" in _ and not ".py" in _:
                sys.exit("Not a CSV file")
        selected = sys.argv[1]
        with open(selected) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "name" in row:
                    surname, name = row["name"].split(", ")
                    lname.append(name)
                    lsurname.append(surname)

                    lhouse.append(row["house"])

        selected = sys.argv[2]
        with open(selected, "w") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for _ in range(len(lname)):
                writer.writerow({
                    "first": lname[_],
                    "last": lsurname[_],
                    "house": lhouse[_]
                })

    except FileNotFoundError:
        sys.exit("File does not exist")


main()
