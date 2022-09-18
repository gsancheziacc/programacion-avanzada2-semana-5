from src.Persona import Persona
from src.Profesion import Profesion


class Profesional(Persona, Profesion):
    # Constructor
    def __init__(self, rut, nombre, apellidos, nacimiento, profesion, area):
        Persona.__init__(self, rut, nombre, apellidos, nacimiento)
        Profesion.__init__(self, profesion, area)

    # Destructor
    def __del__(self):
        print("Destruyendo objeto de tipo profesional con nombre: " + self.obtener_nombre_completo())

    # String
    def __str__(self):
        return "Profesional: " + self.obtener_nombre_completo() + " de la profesión " + self.glosa