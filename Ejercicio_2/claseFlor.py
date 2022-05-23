class Flor:
    __numero = 0
    __nombre = ""
    __color = ""
    __descripcion = ""

    def __init__(self, numero, nombre, color, descripcion):
        self.__numero = int(numero)
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descripcion

    def __str__(self):
        return f"{self.__numero}. {self.__nombre} {self.__color}"

    def getNombre(self):
        return self.__nombre

    def getColor(self):
        return self.__color

    def getNumero(self):
        return self.__numero

