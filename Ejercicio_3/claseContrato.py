class Contrato:
    __fecha_inicio = ""
    __fecha_fin = ""
    __pago_mensual = 0
    __jugador = None
    __equipo = None

    def __init__(self, fecha_inicio, fecha_fin, pago, jugador, equipo):
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__pago_mensual = int(pago)
        self.__jugador = jugador
        self.__equipo = equipo

    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo

    def getFechaInicio(self):
        return self.__fecha_inicio

    def getFechaFin(self):
        return self.__fecha_fin

    def getPago(self):
        return self.__pago_mensual

