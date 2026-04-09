import emoji


def main():
    inquiry = input("Input: ")
    print(f"Output: " + emoji.emojize(inquiry, language="alias"))


main()
