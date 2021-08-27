# is => es 
# is not => no es
frutas =['carambola', 'guayaba', 'higo', 'malecon']
fruta = 'carambola'
# el 'is not'  se usa mas que todo para validar si las variables a comparar estan apuntando a la misma direccion de memoria o no
print( fruta is frutas)

print(id(fruta))
print(id(frutas))

# el 'is not' se usa mas que todo para validar si las variables a comparar estan apuntando a la misma dierccion de memoria o no
# las variables que son coleccion de datos como listas, tuplas y direccionarios son variables mutables
# Las otras Variables (int, str float) son variables inmutables

frutas2 = frutas
frutas2.append('freso')
print(frutas)
print(id(frutas2))
print(id(frutas))
print(frutas2 is frutas)
# Las dos variables NO COMPARTEN la misma ubicacion de memora
print(fruta is frutas)

# avriables mutables e inmutables
#

