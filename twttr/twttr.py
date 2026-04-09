def main():
    response = input(f"Input: ")
    print(abreviate(response))


def abreviate(response):
    i=0
    while i < len(response):
        if response[i].lower() == "a" or response[i].lower() == "e" or response[i].lower() == "i" or response[i].lower() == "o" or response[i].lower() == "u":
            response = response.replace(response[i], "")
        else:
            i += 1
    return response

main()
