from Aparato import Aparato

class Heladera(Aparato):
    __capacidad = 0
    __freezer = None
    __ciclica = None

    def __init__(self, marca, modelo, color, origen, base, capacidad, freezer, ciclica):
        super().__init__(marca, modelo, color, origen, base)
        self.__capacidad = capacidad
        self.__freezer = freezer
        self.__ciclica = ciclica

    def porcentaje(self):
        c = 1
        if self.__freezer:
            c += 0.05
        else:
            c += 0.01
        if self.__ciclica:
            c += 0.1
        return c

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
                freezer=self.__freezer,
                ciclica=self.__ciclica
            )
        )
        return d
