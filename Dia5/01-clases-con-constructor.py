class Persona:
    # un constructor es una metodo propio de las clases que se llamará cuando se cree una isntancia 
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento


    def saludar(self):
        print(f"Hola {self.nombre}")

    def __str__(self):
        """Metodo que sire para que cuando vayamos a llamar a imprimir el objero, se modifique por algo mas entendible"""
        return self.nombre + "Instancia del objeto"

persona1 = Persona("Eduardo", "01-08-1992")
persona2 = Persona("Wilfredo", "10-04-1995")

print(persona1.nombre)
persona1.saludar()
persona2.saludar()

print(persona1)
