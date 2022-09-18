class Profesion:
    # Constructor
    def __init__(self, nombre, area):
        self.glosa = nombre
        self.area = area

    # Destructor
    def __del__(self):
        print("Destruyendo objeto de tipo profesión con nombre: " + self.glosa)

    # Métodos
    def es_carrera_profesional(self):
        if self.glosa == "Farmacéutico":
            return True
        else:
            return False

    def obtener_codigo(self):
        return self.area[0:3] + " - " + self.glosa[0:3]

