import string
import re


def limpar_string(response):

    response = response.lower()
    response = response.strip()
    response = response.replace("-", " ")

    limpar = str.maketrans("", "", string.punctuation)
    response = response.translate(limpar)

    return response


response = input("Greeting: ")

if re.search("hello", limpar_string(response), re.IGNORECASE):
    print("$0")
elif limpar_string(response)[0] == "h":
    print("$20")
else:
    print("$100")
