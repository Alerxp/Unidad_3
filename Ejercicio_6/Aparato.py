from abc import ABC, abstractmethod

class Aparato(ABC):
    __marca = ""
    __modelo = ""
    __color = ""
    __origen = ""
    __base = 0

    def __init__(self, marca, modelo, color, origen, base):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__origen = origen
        self.__base = int(base)

    @abstractmethod
    def porcentaje(self):
        pass

    def importeVenta(self):
        return int(self.__base * self.porcentaje())

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getColor(self):
        return self.__color

    def getOrigen(self):
        return self.__origen

    def getBase(self):
        return self.__base
