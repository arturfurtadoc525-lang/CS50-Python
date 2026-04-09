import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        error = 0
        while error < 3:
            response = int(input(f"{x} + {y} = "))
            if response == x + y:
                score += 1
                break
            else:
                print("EEE")
                error += 1
        if error == 3:
            print(f"{x} + {y} = {x+y}")
    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
