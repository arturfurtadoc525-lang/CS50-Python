def main():
    grocery()


def grocery():
    list = {}
    while True:
        try:
            inp = input().upper()
            if inp in list:
                list[inp] += 1
            else:
                list[inp] = 1
        except EOFError:
            break
    list = dict(sorted(list.items()))
    for l in list:
        print(f"{list[l]} {l}")


main()
