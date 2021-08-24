# # Condiciones
# # If (si) (edad>18) ... else ...
# edad = int(input("Ingrese su edad: "))

# if edad > 18:
#     print("Puedes vacunarte")
#     print("Sigo en el if")
# # elif => sino si / siempre va a despues de un if o despues de otro elif a diferencia del else este llva una condicion
# # a mas de 65 años
# elif edad < 65 :
#     print("Necesitas tercera dosis")
# else:
#     print("Todavia no puedes vacunarte")

# print("Yo me ejecuto así se cumpla o no se cumpla el if")
# ----------------------------------------------------------

# edad = int(input("Ingrese su edad: "))

# if (edad<18) and (edad>65):
#     print("Puedes Vacunarte")
# elif edad > 65:
#     print("Necesitas tecera dosis")
# else:
#     print("Todavia no puedes vacunarte")


# texto = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
# print(texto)


# numero = int(input("Ingrese numero: "))
# texto1 = "Es un número par" if (numero % 2) == 0 else "Es un número impar"
# print(texto1)

 #------------------------------------------------------
#  print(f"El numero "numero" es par")
#  else:
#  print(f""El numero {numero}" es impar)


# BUCLES

# FOR => Repite desde hasta
# meses = ['AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']

# # si nosotros queremos iterar una coleccion  de datos la mejor foram es mediante un FOR
# for mes in meses:
#     print(mes)
# # a diferencia del manejo de scopes (alcance) de la variable en JS, en python, la variable sigue existiendo fuera del for
# print(mes)



# for numero in range(10):
#     print(numero)
# print('=====================')

# for numero in range(5, 10):
#     print(numero)

# print('======================')
# for numero in range(1,10,2):
#     print(numero)


# numeros1 = [-4, 7, -10, 8, 25, -7]
# acuma=0
# acume=0
# for num in numeros1:
#     if(num>0):
#       acuma+=1
#     else:
#       acume+=1

# print("hay {0} positivos y {1} negativos" . format(acuma, acume))

#=======================================================================
# dado los siguientes numeros:
numeros2 = [1,2,5,9,12,15,17,19,21,39, 45]

multiplo_tres = 0 
multiplo_cinco = 0

for numero2 in numeros2:
    if((numero2%3)==0)&((numero2%5)==0):
        print(f"numtiplos de 15 hay {numero2}")
        continue
    elif((numero2%3)==0):
        multiplo_tres+=1
        print(f"numtiplos de 3 hay {numero2}")
    elif((numero2%5)==0):
        print(f"numtiplos de 5 hay {numero2}")
        multiplo_cinco+=1
       
   
print("----------------------")
print(f"numtiplos de 3 hay {multiplo_tres} y multiplos de 5 hay {multiplo_cinco}")
    

print("==========================")

# ingresar numeros hasta que ese numero sea adivinado
numero_adivinar = 10
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'

while True:
    numero = int(input('Ingresa el numero: '))
    if numero < numero_adivinar:
        print('El numero es mayor que {}'.format(numero))
    elif numero > numero_adivinar:
        print('El numero es menor que {}'.format())




