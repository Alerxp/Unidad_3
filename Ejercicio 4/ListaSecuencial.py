import csv
import numpy as np
from Designacion import Designacion

class Lista:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__lista = np.empty(dimension, dtype=Designacion)
        self.__cantidad = 0
        self.__dimension = dimension

    def testArchivo(self):
        with open('estadistica-designacion-magistrados-federal-nacional-por-genero.csv') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            next(file)
            p = 1
            for row in reader:
                self.insertar(Designacion(row[0], row[1], row[2], row[3], row[4], row[5], row[6]), p)
                p += 1
            self.__lista.resize(self.__cantidad)

    def cargoMujeres(self, cargo):
        print("+-----+-----------------------------------------+")
        print("| Año | Cantidad de mujeres cargo tipo: {:>8}|".format(cargo))
        print("+-----+-----------------------------------------+")
        acum = 0
        i = 0
        while i < self.__cantidad:
            if self.__lista[i].getCargo() == cargo:
                acum += self.__lista[i].getMujeres()
            if i < self.__cantidad-1 and self.__lista[i].getAnio() != self.__lista[i+1].getAnio():
                print("|{:>5}|{:>41}|".format(self.__lista[i].getAnio(), acum))
                print("+-----+-----------------------------------------+")
                acum = 0
            i += 1
        print("|{:>5}|{:>41}|".format(self.__lista[i-1].getAnio(), acum))
        print("+-----+-----------------------------------------+")

    def cantidadAgentes(self, materia, cargo, anio):
        pos = self.buscar(anio)
        acum = 0
        if pos:
            while pos-1 < self.__cantidad and self.__lista[pos-1].getAnio() == anio:
                if self.__lista[pos-1].getMateria() == materia and self.__lista[pos-1].getCargo() == cargo:
                    acum += self.__lista[pos-1].getVarones()
                    acum += self.__lista[pos-1].getMujeres()
                pos += 1
        return acum

    def vacia(self):
        return self.__cantidad == 0

    def insertar(self, x, p):
        if p in range(1, self.__cantidad+2):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__lista.resize(self.__dimension)
            if p == self.__cantidad+1:
                self.__lista[self.__cantidad] = x
                self.__cantidad += 1
            else:
                for i in range(self.__cantidad-p+1):
                    self.__lista[self.__cantidad-i] = self.__lista[self.__cantidad-i-1]
                self.__lista[p - 1] = x
                self.__cantidad += 1
        else:
            print("{}".format("Lista vacía, sólo puede insertar un elemento en la posición 1" if self.vacia()
                              else f"Error: rango de posiciones disponibles [1, {self.__cantidad+1}]"))

    def suprimir(self, p):
        if p in range(1, self.__cantidad+1):
            if p == self.__cantidad:
                self.__cantidad -= 1
            else:
                for i in range(self.__cantidad-p+1):
                    self.__lista[i+(p-1)] = self.__lista[i+p]
                self.__cantidad -= 1
        else:
            print("{}".format("Lista vacía" if self.vacia()
                              else f"Error: rango de posiciones disponibles [1, {self.__cantidad}]"))

    def recuperar(self, p):
        if not self.vacia():
            try:
                pos = int(p)
                if pos in range(1, self.__cantidad+1):
                    return self.__lista[pos-1]
                else:
                    print(f"Error: rango de posiciones disponibles [1, {self.__cantidad}]")
            except ValueError:
                print(f"Error: la posición debe ser un número entero")
        else:
            print("Lista vacía")

    def buscar(self, x):
        p = None
        if not self.vacia():
            i = 0
            while i < self.__cantidad and self.__lista[i].getAnio() != x:
                i += 1
            if i < self.__cantidad:
                p = i+1
        return p

    def primero(self):
        if not self.vacia():
            return self.__lista[0]
        else:
            print("Lista vacía")

    def ultimo(self):
        if not self.vacia():
            return self.__lista[self.__cantidad-1]
        else:
            print("Lista vacía")

    def recorrer(self):
        print("[", end="")
        for i in range(self.__cantidad):
            if i < self.__cantidad - 1:
                print(f"{self.__lista[i]}, ", end="")
            else:
                print(self.__lista[i], end="")
        print("]")
