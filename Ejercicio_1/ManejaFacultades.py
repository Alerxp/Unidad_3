import csv
from claseFacultad import Facultad

class ManejaFacultades:
    __facultades = []

    def __init__(self):
        self.__facultades = []
    """
    def agregaFacultades(self):
        with open("Facultades.csv") as file:
            reader = csv.reader(file, skipinitialspace=True)
            fila_facu = next(reader)
            flag = True
            while flag:
                self.__facultades.append(Facultad(int(fila_facu[0]), fila_facu[1], fila_facu[2], fila_facu[3], fila_facu[5]))
                fila_carrera = next(reader)
                while flag and fila_facu[0] == fila_carrera[0]:
                    try:
                        self.__facultades[int(fila_facu[0]) - 1].agregaCarrera(fila_carrera)
                        fila_carrera = next(reader)
                    except StopIteration:
                        flag = False
                fila_facu = fila_carrera
    """
    def testFacultades(self):
        with open("Facultades.csv") as file:
            reader = csv.reader(file, skipinitialspace = True)
            ant = -1
            for row in reader:
                aux = int(row[0])
                if ant != aux:
                    self.__facultades.append(Facultad(int(row[0]), row[1], row[3], row[3], row[5]))
                    ant = aux    # guarda el código de la Facultad
                else:
                    self.__facultades[aux - 1].agregaCarrera(row)

    def muestraFacultad(self, codigo):
        print(self.__facultades[codigo - 1])

    def buscaCodigo(self, codigo):
        rta = False
        i = 0
        while i < len(self.__facultades) and self.__facultades[i].getCodigo() != codigo:
            i += 1
        if i < len(self.__facultades):
            rta = True
        return rta

    def buscaNombre(self, nombre):
        flag, rta = False, None
        i, j = 0, 0
        while i < len(self.__facultades) and not flag:
            j = 0
            while j < len(self.__facultades[i].getCarreras()) and self.__facultades[i].getCarreras()[j].getNombre().lower() != nombre:
                j += 1
            if j < len(self.__facultades[i].getCarreras()):
                flag = True
            i += 1
        if flag:
            rta = f"Código: {i}.{j + 1} - {self.__facultades[i - 1].getNombre()}, {self.__facultades[i - 1].getLocalidad()}"
        return rta
