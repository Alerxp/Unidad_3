from Docente import Docente
from Investigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoria = ""
    __importe = 0

    def __init__(self, cuil, apellido, nombre, basico, antiguedad,
                 area, tipo, carrera, cargo, catedra, categoria, importe):
        super().__init__(cuil, apellido, nombre, basico, antiguedad,
                         area, tipo, carrera, cargo, catedra)
        self.__categoria = categoria
        self.__importe = importe

    def getCategoria(self):
        return self.__categoria

    def getImporte(self):
        return self.__importe

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Categoría: {}\nImporte extra: ${}".format(self.__categoria, self.__importe))

    def __gt__(self, other):
        return self.getNombre() > other.getNombre()

    def porcentaje(self):
        c = Docente.porcentaje(self)
        return c + ((self.__importe * 100) / Docente.getBasico(self))

    def setImporte(self, importe):
        self.__importe = importe

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                basico=super().getBasico(),
                antiguedad=super().getAntiguedad(),
                area=super().getArea(),
                tipo=super().getTipo(),
                carrera=super().getCarrera(),
                cargo=super().getCargo(),
                catedra=super().getCatedra(),
                categoria=self.__categoria,
                importe=self.__importe
            )
        )
        return d
