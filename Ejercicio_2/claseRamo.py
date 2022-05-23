from claseFlor import Flor

class Ramo:
    __tamano = ""
    __flores = []

    def __init__(self, tamano, flores):    # flores: referencias a instancias de la clase Flor
        self.__tamano = tamano
        self.__flores = []
        self.agregaFlores(flores)

    def agregaFlores(self, flores):
        for flor in flores:
            if isinstance(flor, Flor):
                self.__flores.append(flor)

    def __str__(self):
        s = f"\nRamo {self.__tamano}:"
        for flor in self.__flores:
            s += f"\n{flor}"
        return s

    def getTamano(self):
        return self.__tamano

    def getFlores(self):
        return self.__flores

