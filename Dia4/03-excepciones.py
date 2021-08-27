try:
    numero = 5 / 1
    print(f"El numero es {numero}")
    # numero = 1000/0
    # sumar = 1 + '1'
except ZeroDivisionError:
    print("Hubo un error al hacer la division")
except TypeError:
    print("No se puede sumar entre string y numeros")
except:
    print("Error desconocido")
else:
    print("Todo bien")
finally:
    print("Igual me ejecuto")


# finally => no importa si la operacion salio bien o hubo errores, igual se ejecutará

# else => para usar el else tenemos que obligatoriamente DECLARAR un except, y este se ejecutará cuando no ingresa a ningun except (cuando la oepracion no tuvo errores) 

print("soy un ejemplo")


# Ingresar 4 numeros, si uno de ellos no es un numero entonces no tomarlo en cuenta y volver a pedir hasta que tengamos los 4 numeros
# ingresa un numero: 1
# inrgesa un numero: 2
# ingresa un numero: a
# ingresa un numero: 4
# ingresa un nuermo: f
# ingresa un numero: 10
# los numeros son: [1,2,4,10]
numero1=[]
for i in range(4):
    try:
        numero = int(input("ingrese numero: "))
        analisis = numero/1 
    except TypeError:
        print("este no es un numero, vuelva a ingresar")
        numero = int(input("ingrese numero: "))
    else:
        numero1.append(numero) 
    finally:
        print("Igual me ejecuto")

print(numero1)

# Mismo ejemplo hecho por el profe

numeros = []
while len(numeros) != 4:
    try:
        numero = int(input("Ingresa un numero: "))
        numeros.append(numero)
    except:
        pass
print(numeros) 