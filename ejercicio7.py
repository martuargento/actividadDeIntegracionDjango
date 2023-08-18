class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, nuevaEdad):
        self.__edad = nuevaEdad
        
    def get_dni(self):
        return self.__dni
    
    def set_dni(self, nuevoDni):
        self.__dni = nuevoDni   
        
    def mostrar(self):
        return (f'Nombre: {self.__nombre}, Edad: {self.__edad}, Dni: {self.__dni}')
    
    def Es_mayor_de_edad(self):
        if int(self.__edad) >= 18:
            return True
        else:
            return False


"""  
Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. 
Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. 
El atributo no se puede modificar directamente, 
sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, 
si la cantidad introducida es negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. 
La cuenta puede estar en números rojos.

"""

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular

    def set_titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        return f"Titular: {self.__titular.mostrar()}, Cantidad: {self.__cantidad}"

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


# Ejemplo de uso
persona1 = Persona("Juan", 25, "12345678")
cuenta1 = Cuenta(persona1, 1000.0)

print(persona1.mostrar())
print("Es mayor de edad:", persona1.Es_mayor_de_edad())

print(cuenta1.mostrar())
cuenta1.ingresar(500.0)
cuenta1.retirar(200.0)
print(cuenta1.mostrar())
