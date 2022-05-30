class Calefactor:
    __marca = ""
    __modelo = ""

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        return f"Marca: {self.__marca} - Modelo: {self.__modelo}"

    def getMarca(self):
        return self.__marca

    def getmodelo(self):
        return self.__modelo

