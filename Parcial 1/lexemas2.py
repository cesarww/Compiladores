file_path = 'texto3.txt'

lista_palabras = ''

with open(file_path, 'r') as file:
    content = file.read()

    comentario = '//'

    lineas = content.split('\n')
    # print(lineas)
    for linea in lineas:
        if comentario in linea:
            linea = linea.split(comentario)[0]

        # print(linea.strip())

        lista_palabras += linea.strip() + ' '

conteo_palabras = {}

palabras = lista_palabras.split()

for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

palabras_unicas = list(conteo_palabras.keys())

for palabra in palabras_unicas:
    print(f'{palabra}: {conteo_palabras[palabra]}')