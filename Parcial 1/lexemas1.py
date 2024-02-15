texto = 'las manzanas son las frutas preferidas de las maestras'
lista_palabras = texto.split()

conteo_palabras = {}

for palabra in lista_palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

palabras_unicas = list(conteo_palabras.keys())

for palabra in palabras_unicas:
    print(f'{palabra}: {conteo_palabras[palabra]}')