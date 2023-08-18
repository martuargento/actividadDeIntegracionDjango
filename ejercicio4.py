"""
Escribir una función que reciba una cadena de caracteres 
y devuelva un diccionario con cada palabra que contiene 
y la cantidad de veces que aparece (frecuencia). 
Escribir otra función que reciba el diccionario 
generado con la función anterior y devuelva una tupla 
con la palabra más repetida y su frecuencia
"""

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


def palabra_mas_repetida(resultado):
    palabra_max = None
    frecuencia_max = 0
    
    for palabra, frecuencia in resultado.items(): #hacemos un for donde en cada iteracion comprobaremos si el valor de aparacion de esa clave, es mayor al que estamos poniendo en las variables creadas para alojar a la palabra que mas aparece junto con su valor de aparicion
        if frecuencia > frecuencia_max: #si la palabra de esta iteracion tiene una frecuncia mayor que a la alojada en frecuencia_max
            palabra_max = palabra #ahora palabra_max es igual a la palabra de esta iteracion
            frecuencia_max = frecuencia #y frecuencia_max es igual al valor de esta iteracion
    
    return palabra_max, frecuencia_max #devolvemos una tupla con la palabra con mas apariciones y su valor de frecuencia



entrada = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(entrada)

palabra_repetida, frecuencia_palabra_repetida = palabra_mas_repetida(resultado) #metemos en palabra repetida lo que devuelve palabra_max de la funcion palabra_mas_repetida(), y metemos en frecuencia_palabra_repetida lo que devuelve la variable frecuencia_max de la misma funcion

print("Frecuencia de palabras:") #imprimos las palabras y las frecuencia de apariciones como el ejercicio anterior
for palabra, frecuenciaDeAparacion in resultado.items():
    print(f"'{palabra}': {frecuenciaDeAparacion}")

#imprimos la palabra mas repetida y su frecuencia de aparicion
print(f"Palabra más repetida: '{palabra_repetida}', Frecuencia: {frecuencia_palabra_repetida}")