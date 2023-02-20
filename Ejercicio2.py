import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

r = requests.get('https://imdb-api.com/en/API/Trailer/k_n4fp5ybj/tt0088509')

trailer = r.json()["linkEmbed"]

pp.pprint(trailer)
