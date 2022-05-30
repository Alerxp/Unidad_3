from Calefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __potencia = 0

    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo)
        self.__potencia = int(potencia)

    def __str__(self):
        return super().__str__() + f" - {self.__potencia}W"

    def getPotencia(self):
        return self.__potencia

