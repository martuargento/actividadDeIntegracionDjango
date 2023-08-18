
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


class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
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
            
            
"""  
Vamos a definir ahora una “Cuenta Joven”, 
para ello vamos a crear una nueva clase CuantaJoven 
que deriva de la clase creada en el punto 7. 
Cuando se crea esta nueva clase, además del titular y la cantidad 
se debe guardar una bonificación que estará expresada en tanto por ciento. 
Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta 
tienen que ser mayor de edad, por lo tanto 
hay que crear un método es_titular_valido() 
que devuelve verdadero si el titular es mayor de edad pero menor de 25 años 
y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” 
y la bonificación de la cuenta.
"""


class CuentaJoven(Cuenta): #heredamos de la clase cuenta
    def __init__(self, titular=None, cantidad=0.0, bonificacion=20.0):
        super().__init__(titular, cantidad)
        if(self.es_titular_valido()):
            self.__bonificacion = bonificacion
        else:
            self.__bonificacion = 0.0    

    def get_bonificacion(self):
        return self.__bonificacion

    def set_bonificacion(self, nueva_bonificacion):
        self.__bonificacion = nueva_bonificacion

    def es_titular_valido(self):
        if self.get_titular().get_edad() >= 18 and self.get_titular().get_edad() < 25:
            return True
        return False

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        return f"Cuenta Joven - {super().mostrar()}, Bonificación: {self.__bonificacion}%"





martin = Persona("Martin Nuñez", 32, "35376006")
roberto = Persona("Roberto Perez", 22, "33245234")


cuenta1 = CuentaJoven(martin)
cuenta2 = CuentaJoven(roberto)


print(cuenta1.mostrar())
print(cuenta2.mostrar())


