from datetime import date
import inflect
import sys

class Pessoa:
    def __init__(self, data_input):
        try:
            dataF = date.fromisoformat(data_input)
        except ValueError:
            sys.exit("VallueError")
        self.day = dataF.day
        self.month = dataF.month
        self.year = dataF.year


    def __str__(self):
        return f"{self.extenso.capitalize()}"

    @property
    def extenso(self):
        hoje = date.today()
        bDay = date(self.year, self.month, self.day)
        age = hoje - bDay

        p = inflect.engine()
        extenso = p.number_to_words(age.days*1440, andword= '')

        return extenso




def main():
    artur = Pessoa(input("Date of Birth: "))
    print(f"{artur} minutes")


...


if __name__ == "__main__":
    main()
