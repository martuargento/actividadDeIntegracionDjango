def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    return (a * b) // calcular_mcd(a, b)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

mcm = calcular_mcm(numero1, numero2)
print(f"El mínimo común múltiplo entre {numero1} y {numero2} es {mcm}")