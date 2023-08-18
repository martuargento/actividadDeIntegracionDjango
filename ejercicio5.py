"""
Sabiendo que ValueError es la excepción que se lanza  
cuando no podemos convertir una cadena de texto en su valor numérico, 
escriba una función get_int() que lea un valor entero del usuario 
y lo devuelva, iterando mientras el valor no sea correcto. 
Intente resolver el ejercicio tanto de manera iterativa como recursiva.
"""

def get_int():
    try: #intentamos lo siguiente:
        valor = int(input("Ingrese un valor entero: ")) #el usuario ingresa un numero entero
        return valor #si lo anterior se realizo correctamente devolvemos el valor entero ingresado por el usuario
    
    except ValueError:  #en caso de que de ValueError porque lo anterior no pudo realizarse ya que el usuario coloco un numero que no era entero..
        print("Error: El numero ingresado no es un numero entero. Intente nuevamente.") #imprimimos que hay un error porque el numero ingresado no fue un numero entero, y decimos que intente nuevamente
        return get_int() #y volvemos a llamar a la funcion para que se repita el ciclo hasta que el usuario ingrese correctamente un numero entero

entero = get_int() #el valor entero devuelto por la funcion lo almacenamos en la variable entero
print(f"El valor entero ingresado es: {entero}") #e imprimimos el numero entero ingresado
