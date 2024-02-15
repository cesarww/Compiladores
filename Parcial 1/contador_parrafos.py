nombre_archivo = 'texto2.txt'

with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()

    parrafos = contenido.count('\n\n') + 1

    palabras = len(contenido.split())

    caracteres = len(contenido)

    print(f"Parrafos: {parrafos}")
    print(f"Palabras: {palabras}")
    print(f"Caracteres: {caracteres}")