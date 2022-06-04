from Aparato import Aparato

class Lavarropas(Aparato):
    __capacidad = 0
    __rpm = 0
    __programas = 0
    __carga = ""

    def __init__(self, marca, modelo, color, origen, base, capacidad, rpm, programas, carga):
        super().__init__(marca, modelo, color, origen, base)
        self.__capacidad = capacidad
        self.__rpm = rpm
        self.__programas = programas
        self.__carga = carga

    def porcentaje(self):
        c = 1
        if self.__capacidad > 5:
            c += 0.03
        else:
            c += 0.01
        return c

    def getCarga(self):
        return self.__carga

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=super().getMarca(),
                modelo=super().getModelo(),
                color=super().getColor(),
                origen=super().getOrigen(),
                base=super().getBase(),
                capacidad=self.__capacidad,
                rpm=self.__rpm,
                programas=self.__programas,
                carga=self.__carga
            )
        )
        return d
