response = input("Expresion: ")
x, y, z = response.split(" ")


def calculator(response, x, y, z):
    if y == "+":
        response = x + z
        return response
    elif y == "-":
        response = x - z
        return response
    elif y == "/":
        response = x / z
        return response
    elif y == "*":
        response = x * z
        return response


print(float(calculator(response, int(x), y, int(z))))
