class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad  # Usamos doble guión bajo para hacer el atributo privado

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


# Ejemplo de uso:
cuenta1 = Cuenta("Juan Pérez")
cuenta1.mostrar()

cuenta1.ingresar(1000)
cuenta1.mostrar()

cuenta1.retirar(300)
cuenta1.mostrar()

cuenta1.set_titular("María Rodríguez")
cuenta1.set_cantidad(2000)
cuenta1.mostrar()
