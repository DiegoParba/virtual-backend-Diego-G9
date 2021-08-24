class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def acelerar(self):
        print("EL auto esta acelerando 🚗")

    def estado(self):
        return f"Marca: {self.marca} \nModelo: {self.mdelo} \nRuedas: {self.numero_ruedas}"


class Auto(Vehiculo):
    def __init__(self, sunroof, amrca, modelo):
        self.sunroof = sunroof
        super().__init__(marca, modelo, 4)

    def estado(self):
        resultado_padre = super().estado()
        return resultado_padre + f"\nSunroof: {self.sunroof}"


class Camion(Vehiculo):
    def __init__(self, numero_cambios, amrca, modelo):
        self.numero_cambios = numero_cambios
        super().__init__(marca, modelos, 8)
    
    # def saludar(self)
    #    print() 

    # def saludar (self, nombre)

objAuto = Auto(True, "Chevrolet", "Alto")
print(objAuto.marca)
print(objAuto.estado())

objCamion = Camion(7, "Scania", "F100")
print(objAuto.estado())
# objCamion.saludar("Eduardo")
# en PYTHON EL POLIMORFISMO NO funciona de la misma manera que los otros lenguajes
