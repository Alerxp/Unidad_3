class Provincia:
    __nombre: str
    __supAfectada: float

    def __init__(self, nom, sup):
        self.__nombre = nom
        self.__supAfectada = float(sup)

    def __gt__(self, other):
        return self.__supAfectada > other.__supAfectada

    def __le__(self, other):
        return self.__supAfectada <= other.__supAfectada

    def getNombre(self):
        return self.__nombre

    def getSuperficie(self):
        return self.__supAfectada
