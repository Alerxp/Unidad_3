class Designacion:
    __anio: int
    __justicia: str
    __cargo: str
    __instancia: str
    __materia: str
    __varones: int
    __mujeres: int

    def __init__(self, anio, justicia, cargo, instancia, materia, varones, mujeres):
        self.__anio = int(anio)
        self.__justicia = justicia
        self.__cargo = cargo
        self.__instancia = instancia
        self.__materia = materia
        self.__varones = int(varones)
        self.__mujeres = int(mujeres)

    def getCargo(self):
        return self.__cargo

    def getVarones(self):
        return self.__varones

    def getMujeres(self):
        return self.__mujeres

    def getAnio(self):
        return self.__anio

    def getMateria(self):
        return self.__materia
