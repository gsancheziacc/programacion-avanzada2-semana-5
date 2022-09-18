from datetime import date


class Persona:
    # Constructor
    def __init__(self, rut, nombre, apellidos, fecha_nacimiento):
        self.rut = rut
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento

    # Destructor
    def __del__(self):
        print("Destruyendo objeto de tipo persona con nombre: " + self.nombre)

    # Métodos
    def obtener_nombre_completo(self):
        return "%s %s" % (self.nombre, self.apellidos)

    def calcular_edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
                    (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
