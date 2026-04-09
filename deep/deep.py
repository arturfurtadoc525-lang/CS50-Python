import string

test = ["42", "forty two"]


def limpar_string(response):
    response = response.lower()
    response = response.strip()
    response = response.replace("-", " ")

    limpar = str.maketrans("", "", string.punctuation)
    response = response.translate(limpar)

    return response


response = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything?"
)

if limpar_string(response) == test[0]:
    print(f"Yes")
elif limpar_string(response) == test[1]:
    print(f"Yes")
else:
    print(f"No")
