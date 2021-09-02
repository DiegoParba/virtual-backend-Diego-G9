from faker import Faker
import faker
from faker.providers import person
# LIBRERIA FAKER PARA GENERAR INFORAMCION FALSA EN UNA BASE DE DATOS
fake = Faker()
fake.add_provider(person)

for alumno in range(1, 51):
    nombre = fake.first_name()
    apellido = fake.last_name()
    correo = fake.email()
    query = f"INSERT INTO ALUMNOS (nombre, apellido, correo) VALUES ('{nombre}', '{apellido}', '{correo}');"
    print(query)

for alumnos_curso in range(75):
    curso = fake.random_int(1, 5)
    alumno = fake.random_int(1, 50)
    query = f"INSERT INTO PUENTE_CURSOS (ID_ALUMNO, ID_CURSO) VALUES ({alumno}, {curso});"
    print(query)