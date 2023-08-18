def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para considerar mayúsculas y minúsculas iguales
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

entrada = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(entrada)

print("Frecuencia de palabras:")
for palabra, frec in resultado.items():
    print(f"'{palabra}': {frec}")
