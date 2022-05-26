import csv, numpy as np
from claseEquipo import Equipo
from datetime import date
from dateutil.relativedelta import relativedelta

class ManejadorEquipo:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__equipos = np.empty(dimension, dtype=Equipo)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregaEquipo(self, equipo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__equipos.resize(self.__dimension)
        self.__equipos[self.__cantidad] = equipo
        self.__cantidad += 1

    def testEquipos(self):
        with open("Equipos.csv") as file:
            reader = csv.reader(file, delimiter=";")
            next(file)
            for row in reader:
                equipo = Equipo(row[0], row[1])
                self.agregaEquipo(equipo)
            self.__equipos.resize(self.__cantidad)

    def buscaEquipo(self, nombre):
        equipo = None
        i = 0
        while i < self.__cantidad and self.__equipos[i].getNombre().lower() != nombre:
            i += 1
        if i < self.__cantidad:
            equipo = self.__equipos[i]
        return equipo

    def contratosQueVencen(self, nombre):
        equipo = self.buscaEquipo(nombre)
        if equipo:
            hoy = date.today()
            for contrato in equipo.getContratos():
                fecha = contrato.getFechaFin()
                vencimiento = date(int(fecha[6:]), int(fecha[3:5]), int(fecha[:2]))
                if hoy + relativedelta(months=6) == vencimiento:
                    print(contrato.getJugador())
        else:
            print("*** EL NOMBRE DEL EQUIPO NO ES CORRECTO ***")

    def importeContratos(self, nombre):
        equipo = self.buscaEquipo(nombre)
        importe = 0
        if equipo:
            for contrato in equipo.getContratos():
                importe += contrato.getPago()
        else:
            print("*** EL NOMBRE DEL EQUIPO NO ES CORRECTO ***")
        return importe

