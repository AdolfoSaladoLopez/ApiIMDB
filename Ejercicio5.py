import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

r = requests.get('https://imdb-api.com/en/API/SearchTitle/k_n4fp5ybj/Akira%201988')

pelicula = r.json()["results"][0]
imagen = pelicula["image"]
imagen_resolucion = 'https://m.media-amazon.com/images/M/MV5BM2ZiZTk1ODgtMTZkNS00NTYxLWIxZTUtNWExZGYwZTRjODViXkEyXkFqcGdeQXVyMTE2MzA3MDM@._V1_UX2000_CR0,660,2000,3000_AL_.jpg'
reporte = 'https://imdb-api.com/en/API/Report/k_n4fp5ybj/tt0094625'

print("La imagen de la película original es: " + str(imagen))
print("La imagen con una resolución 2000x3000 es: " + str(imagen_resolucion))
print("El reporte es el siguiente: " + str(reporte))
