import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if not level < 0 and isinstance(level, (int)):
                game(level)
                return
        except ValueError:
            pass


def game(level):
    win = False
    number = int(random.randint(1, level))
    while win == False:
        response = int(input("Guess: "))
        if response > 0:
            if response > number:
                print("Too large!")
            elif response < number:
                print("Too small!")
            else:
                print("Just right!")
                win = True
    return


main()
