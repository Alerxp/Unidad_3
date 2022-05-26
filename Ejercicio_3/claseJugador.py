class Jugador:
    __nombre = ""
    __dni = ""
    __ciudad_natal = ""
    __pais_origen = ""
    __fecha_nacimiento = ""

    def __init__(self, nombre, dni, ciudad, pais, fecha):
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudad_natal = ciudad
        self.__pais_origen = pais
        self.__fecha_nacimiento = fecha

    def __str__(self):
        return f"{self.__nombre} - DNI: {self.__dni}"

    def getDNI(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

