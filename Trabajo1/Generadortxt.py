import itertools

def generador_palabras(length):
    # Genera todas las combinaciones posibles de lo que le pongas entre comillas para la longitud dada
    string = [''.join(x) for x in itertools.product('abc', repeat=length)]
    return string

def escribir_palabras(palabras, archivo):
    # Escribe las palabras en un archivo de texto
    with open(archivo, 'w') as file:
        for palabra in palabras:
            file.write(palabra + '\n')

if __name__ == "__main__":
    maxima_long = 10

    # Genera palabras para todas las longitudes hasta maxima_long
    combinaciones = []
    for n in range(1, maxima_long + 1):
        palabras = generador_palabras(n)
        combinaciones.extend(palabras)

    nombre_archivo = "palabras_abc.txt"
    escribir_palabras(combinaciones, nombre_archivo)
