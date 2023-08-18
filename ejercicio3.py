def contar_palabras(cadena):
    palabras = cadena.split() #.split() va cortando las palabras, cada vez que hay un espacio, y crea una lista donde mete cada una de esas palabras
    frecuencia = {} #creamos un diccionario vacio
    for palabra in palabras:
        palabra = palabra.lower()  # Convertimos a minúsculas con .lower() para que si se pone MARTIN sea igual a poner martin, sin importar si estan mayusculas o minusculas va a ser lo mismo
        if palabra in frecuencia: #Si la palabra, ya es una clave en el diccionario
            frecuencia[palabra] += 1 #hacemos que el valor de esa clave se incremente en 1
        else:
            frecuencia[palabra] = 1 #Si la palabra no existe en el diccionario, insertamos la palabra y le pones de valor 1
    
    return frecuencia

entrada = str(input("Ingrese una cadena de texto: "))
resultado = contar_palabras(entrada)

print("Frecuencia de palabras:")
for palabra, frecuenciaDeAparacion in resultado.items(): #recorremos el diccionario resultante, poniendo en cada iteracion, del diccionario, la clave en palabra, y el valor en FrecuenciaDeAparacion
    print(f"'{palabra}': {frecuenciaDeAparacion}") #imprimos las palabras y las frecuencias de aparaciones
