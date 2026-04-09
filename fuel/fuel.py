from fractions import Fraction


def main():
    fuel()


def fuel():
    while True:
        try:
            tank = input("Fraction: ")
            tank = Fraction(tank)

            if (
                tank.numerator > tank.denominator
                or tank.numerator < 0
                or tank.denominator < 0
            ):
                raise ValueError

            tank = round(float(tank) * 100)

            if tank <= 1:
                print("E")
            elif tank >= 99:
                print("F")
            else:
                print(f"{tank}%")
            break
        except (ValueError, ZeroDivisionError):
            print(f"Digite um valor aceitável (ex.: 2/3)")


main()
