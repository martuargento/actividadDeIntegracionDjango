def calcular_mcd(a, b):
    while b:
        nuevo_a = b
        nuevo_b = a % b
        a, b = nuevo_a, nuevo_b
    return a

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

mcd = calcular_mcd(numero1, numero2)
print(f"El máximo común divisor entre {numero1} y {numero2} es {mcd}")