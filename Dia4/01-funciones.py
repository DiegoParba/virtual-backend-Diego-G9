# una funcion es un bloque de codigo que se va a ejecutar cuantas veces sea llamda la funcion

def saludar():
    print("Hola buenas tardes")

saludar()


def saludarPersona(nombre):
    print(f"Hola {nombre} como te va")

saludarPersona("Diego")



def sin_nombre():
    """Funcion que no hace nada y solamente es de muestra"""
    print("yo soy una funcion sin nombre")


sin_nombre()


#las funciones pueden recibir parametros y estos pueden ser opcionales
def registro(nombre, correo=None):
    print("Registro exitoso")

registro("Diego")
registro("Diego", "ederivoman@gmail.com")
#registro()

#Crear una funcion llamda identificacion e n la cual se reciba el nombre apellido y la nacionalidad del cliente, si en el caso no se pasa la nacionalidad entonces sera Peruano, imprimier el resultado en forma de un diccionaio

def identificacion(nombre, apellido, nacionalidad="Peruana"):
    resultado ={
    "nombre": nombre,
    "apellido":apellido,
    "nacionalidad": nacionalidad
    }
    print(resultado)

identificacion("Diego","PAredes","Colombiano")

# todos los parametros que tengan un valor predeterminado SIEMPRE van al final
def sumatoria(num1, num2=10, num3=15):
    print(num1+num2+num3)

sumatoria(10)

# el parametro que tiene el simbolo * es un parametro de python que sirve para almancenar n valores
# todos los valores que pasemos 

def alumnos(*args):
    print(args)

alumnos("Eduardo", "Siannet", "Pablo", "Fernando", "Rick", "Jhonatan")

def tareas(nombre, apellido, *args):
    print("ok")


tareas("Eduardo", "martinez", "1", "2", 3)


# en la funcion alumnos_notas se recibira una cantidad N de alumnos en la cual se debe indicar cuantos aprobaron y cuantos desaprobaron siendo la nota minima 11
def alumnos_notas(*args):
    
    aprobados = 0
    desaprobados = 0
    for alumno in args:
        if(alumno['promedio'] > 10):
            aprobados += 1
        else:
            desaprobados +=1
    print(f"Hay {aprobados} alumnos aprobados y {desaprobados} alumnos desaprobados")

#los Json en python son llamados biblioteca

alumnos_notas(
    {"nombre":"Raul", "promedio": 17},
    {"nombre": "Roxana", "promedio": 20},
    {"nombre": "Alfonso", "promedio": 10},
    {"nombre": "Pedro", "promedio": 8},
    {"nombre": "Katherine", "promedio": 16}
)

# keyword arguments => es muy similiar a los *args solo con la diferencia que los kwargs usan el nombre del parametro (nombre="Eduardo")

def indeterminada(**kwargs):
    print(kwargs)

indeterminada(nombre="Diego", apellido="de rivero", nacionalidad="")

