import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

r = requests.get('https://imdb-api.com/en/API/SearchSeries/k_n4fp5ybj/Dragon Ball')

numero_elementos = len(r.json()["title"])

print("Hay un total de " + str(numero_elementos) + " elementos.")
