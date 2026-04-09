def main():
    try:
        order = input("Item: ")
        taqueria(order)
    except EOFError:
        print("")


def taqueria(order):
    total = 0
    store = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00,
    }
    while True:
        try:
            for o in store:
                if o == order.lower():
                    total = total + float(store[order.lower()])
                    print(f"${total:.2f}")
            order = input("Item: ")
        except EOFError:
            break


main()
