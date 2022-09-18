from src.Persona import Persona
from datetime import date
from src.Profesion import Profesion
from src.Profesional import Profesional

persona1 = Persona("1-9", "Juan", "Pérez Rodriguez", date(1995, 5, 4))
print("Imprimir nombre completo " + persona1.obtener_nombre_completo())
print("Imprimir edad " + str(persona1.calcular_edad()))

persona2 = Persona("2-7", "Pedro", "Trejo Meléndez", date(1993, 11, 23))
print("Imprimir nombre completo " + persona2.obtener_nombre_completo())
print("Imprimir edad " + str(persona2.calcular_edad()))

profesion1 = Profesion("Farmacéutico", "Salud")
print("Imprimir si es una carrera profesional: " + str(profesion1.es_carrera_profesional()))
print("Imprimir código de la carrera: " + profesion1.obtener_codigo())

profesion2 = Profesion("Bibliotecario", "Humanista")
print("Imprimir si es una carrera profesional: " + str(profesion2.es_carrera_profesional()))
print("Imprimir código de la carrera: " + profesion2.obtener_codigo())

profesional1 = Profesional(persona1.rut, persona1.nombre, persona1.apellidos, persona1.fecha_nacimiento, profesion1.glosa, profesion1.area)
print(profesional1)