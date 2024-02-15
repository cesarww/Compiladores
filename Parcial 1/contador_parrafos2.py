import re

nombre_archivo = 'texto2.txt'

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()

        parrafos = len(re.split(r'\n\s*\n', contenido))

        palabras = len(contenido.split())
        caracteres = len(contenido)

        print(f"Parrafos: {parrafos}")
        print(f"Palabras: {palabras}")
        print(f"Caracteres: {caracteres}")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")

except Exception as e:
    print(f"Ocurrió un error: {e}")
