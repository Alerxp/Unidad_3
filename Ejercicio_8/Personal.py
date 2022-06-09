from abc import ABC, abstractmethod

class Personal(ABC):
    __cuil = ""
    __apellido = ""
    __nombre = ""
    __basico = 0
    __antiguedad = 0

    def __init__(self, cuil, apellido, nombre, basico, antiguedad,
                 area="", tipo="", carrera="", cargo="", catedra=""):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__basico = int(basico)
        self.__antiguedad = int(antiguedad)

    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getBasico(self):
        return self.__basico

    def getAntiguedad(self):
        return self.__antiguedad

    def mostrarDatos(self):
        print("CUIL: {}\nNombre y Apellido: {} {}\nSueldo básico: ${}\nAntigüedad: {} años".
              format(self.__cuil, self.__nombre, self.__apellido, self.__basico, self.__antiguedad))

    @abstractmethod
    def porcentaje(self):
        pass

    def getSueldo(self):
        return int(self.__basico + (self.porcentaje() * self.__basico) / 100)

    def __gt__(self, other):
        return self.__apellido > other.__apellido

    def setBasico(self, basico):
        self.__basico = basico

