class Carrera:
    __codigo = 0
    __nombre = ""
    __duracion = ""
    __titulo = ""

    def __init__(self, codigo, nombre, duracion, titulo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__titulo = titulo

    def __str__(self):
        return f"{self.__nombre} - {self.__duracion}"

    def getNombre(self):
        return self.__nombre
