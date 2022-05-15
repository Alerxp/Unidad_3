from claseCarrera import Carrera

class Facultad:
    __codigo = 0
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = ""
    __carreras = []

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []

    def agregaCarrera(self, fila):
        # El objeto contenido se crea dentro del objeto continente
        carrera = Carrera(fila[1], fila[2], fila[4], fila[3])
        self.__carreras.append(carrera)

    def __str__(self):
        s = f"===== {self.__nombre} =====\n\n"
        for carrera in self.__carreras:
            s += f"{carrera}\n"
        return s

    def getCodigo(self):
        return self.__codigo

    def getCarreras(self):
        return self.__carreras

    def getNombre(self):
        return self.__nombre

    def getLocalidad(self):
        return self.__localidad
