def main():
    response = input(f"camelCase: ")
    snakeCase(response)
    print(f"snake_case: " + snakeCase(response))


def snakeCase(response):
    hold = ""
    i = 0
    while i < len(response):
        if response[i].isupper():
            hold += "_" + response[i].lower()
        else:
            hold += response[i]
        i += 1
    if hold.startswith("_"):
        hold = hold[1:]
    return hold


main()
