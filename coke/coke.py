def main():
    cokeMachine()


def cokeMachine():
    total = 0
    while total < 50:
        print("Amount Due: " + str(50 - total))
        hold = int(input("Insert Coin: "))
        if hold == 5 or hold == 10 or hold == 25:
            total += hold
            if total >= 50:
                total -= 50
                break
        else:
            print(hold)
            print("Insert a real coin (5, 10 or 25 cents)")
    print("Change Owed: " + str(total))
    return


main()
