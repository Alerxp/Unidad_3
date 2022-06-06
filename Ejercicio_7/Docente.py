from Personal import Personal

class Docente(Personal):
    __carrera = ""
    __cargo = ""
    __catedra = ""

    def __init__(self, cuil, apellido, nombre, basico, antiguedad,
                 area, tipo, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, basico, antiguedad,
                         area, tipo, carrera, cargo, catedra)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Carrera: {}\nCargo: {}\nCátedra: {}".format(self.__carrera, self.__cargo, self.__catedra))

    def porcentaje(self):
        c = super().getAntiguedad()
        if self.__cargo == "simple":
            c += 10
        elif self.__cargo == "semiexclusivo":
            c += 20
        elif self.__cargo == "exclusivo":
            c += 50
        return c

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                basico=super().getBasico(),
                antiguedad=super().getAntiguedad(),
                area="",
                tipo="",
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return d
