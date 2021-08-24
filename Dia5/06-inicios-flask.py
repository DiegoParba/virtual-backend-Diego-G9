from flask import Flask

# __name__ => muestra si el archivo en el cual se esta llamando a la clase Flask es el archivo principal del proyecto, esto se hace para evitar que la isntancia de la case FLask se pueda crear en otros lados (patron de diseño singletton)
app = Flask(__name__)

# si estamos en el archivo principal del proyecto nos imprimira __main__ caso contrario imprimira la ubicacion del archivo
# print(__name__)

# decorador => un patron de softwear que se utiliza para modificar el funcionamioento de una clase o una funcion en particular sin la necesidad de emplear otros metodos como la herencia (coas que no se puede en una funcion comun y corriente)
@app.route('/')
def incio():
    print("Me llamaron!")
    return {
        "message":"Hello world!"
    }
# NOTA: Todo el codigo a implementar siempre debe de ir antes del run()
#el parametro de flask debnug se usa para que no encesitemos bajar y vovler a levantar el servididr cuando hagamos una actualizacion 
#app.run()
app.run(debug=True)