from Aparato import Aparato

class Televisor(Aparato):
    __pantalla = ""
    __pulgadas = 0
    __definicion = ""
    __internet = None

    def __init__(self, marca, modelo, color, origen, base, pantalla, pulgadas, definicion, internet):
        super().__init__(marca, modelo, color, origen, base)
        self.__pantalla = pantalla
        self.__pulgadas = pulgadas
        self.__definicion = definicion
        self.__internet = internet

    def porcentaje(self):
        c = 1
        if self.__definicion == "SD":
            c += 0.01
        elif self.__definicion == "HD":
            c += 0.02
        elif self.__definicion == "FULLHD":
            c += 0.03
        if self.__internet:
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
                pantalla=self.__pantalla,
                pulgadas=self.__pulgadas,
                definicion=self.__definicion,
                internet=self.__internet
            )
        )
        return d
