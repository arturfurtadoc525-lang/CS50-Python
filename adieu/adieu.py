import inflect


def main():
    p = inflect.engine()
    response = []
    while True:
        try:
            response.append(input("Name: "))
        except EOFError:
            break
    print("\n")
    print(f"Adieu, adieu, to " + p.join(response))


main()
