from Personal import Personal

class Investigador(Personal):
    __area = ""
    __tipo = ""

    def __init__(self, cuil, apellido, nombre, basico, antiguedad,
                 area, tipo, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, basico, antiguedad,
                         area, tipo, carrera, cargo, catedra)
        self.__area = area
        self.__tipo = tipo

    def getArea(self):
        return self.__area

    def getTipo(self):
        return self.__tipo

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Area de investigación: {}\nTipo de investigación: {}".format(self.__area, self.__tipo))

    def porcentaje(self):
        return super().getAntiguedad()

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                basico=super().getBasico(),
                antiguedad=super().getAntiguedad(),
                area=self.__area,
                tipo=self.__tipo,
                carrera="",
                cargo="",
                catedra=""
            )
        )
        return d
