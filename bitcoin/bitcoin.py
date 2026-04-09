import requests
import sys


url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=36a607d1305464c4cfca40a6a79d3d114338828efb84db53f834b32e1f904368"
try:
    pega = requests.get(url)
    dataJson = pega.json()

    quant = float(sys.argv[1])
    preço = quant * float(dataJson["data"]["priceUsd"])
    print(f"${float(preço):,.4f}")
except requests.RequestException:
    sys.exit("Erro ao conectar com a API")
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

