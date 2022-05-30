from Calefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula = ""
    __calorias = 0

    def __init__(self, marca, modelo, matricula, calorias):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = int(calorias)

    def __str__(self):
        return super().__str__() + f" - Matrícula: {self.__matricula} - {self.__calorias}kcal/h"

    def getCalorias(self):
        return self.__calorias

