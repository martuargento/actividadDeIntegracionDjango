"""" 
Crear una clase llamada Persona. 
Sus atributos son: nombre, edad y DNI. 

Construya los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. 
Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico 
indicando si es mayor de edad.
"""

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
    
    
martin = Persona("Martin", "32", "35376006")    
print(martin.mostrar())

print(martin.Es_mayor_de_edad())
martin.set_edad("17")
print(martin.Es_mayor_de_edad())

