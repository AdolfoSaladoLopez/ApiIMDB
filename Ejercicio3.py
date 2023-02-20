import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

r = requests.get('https://imdb-api.com/en/API/SeasonEpisodes/k_n4fp5ybj/tt0088509/1/')

numero_episodios = len(r.json()["episodes"])

pp.pprint("La primera temporada tiene un total de " + str(numero_episodios) + " episodios.")
