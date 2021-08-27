from typing import Collection


class Mueble:
    precio = 0.00
    colo = "Blanco"
    especificaciones = []
    tipo = ""

    def indicar_tipo(self):
        return "El tipo es: {}".format(self.tipo)


mueble1 = Mueble()
mueble1.tipo = "Sofa-cama"
print(mueble1.indicar_tipo())

mueble2 = Mueble()
mueble2.tipo = "Silla"
print(mueble2.indicar_tipo())

