import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

r = requests.get('https://imdb-api.com/en/API/SeasonEpisodes/k_n4fp5ybj/tt0088509/1/')

ultimo_episodio = r.json()["episodes"][152]
fecha_publicacion = ultimo_episodio["released"]
descripcion = ultimo_episodio["plot"]

pp.pprint("La fecha de publicación fue: " + str(fecha_publicacion))
pp.pprint("La descripción es la siguiente: " + descripcion)
