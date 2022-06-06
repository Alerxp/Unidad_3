from Personal import Personal

class Apoyo(Personal):
    __categoria = 0

    def __init__(self, cuil, apellido, nombre, basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, basico, antiguedad)
        self.__categoria = int(categoria)

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Categoría: {}".format(self.__categoria))

    def porcentaje(self):
        c = super().getAntiguedad()
        if self.__categoria in range(1, 11):
            c += 10
        elif self.__categoria in range(11, 21):
            c += 20
        elif self.__categoria in range(21, 23):
            c += 30
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
                categoria=self.__categoria
            )
        )
        return d
