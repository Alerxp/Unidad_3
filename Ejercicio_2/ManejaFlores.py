import csv, numpy as np
from claseFlor import Flor

class ManejaFlores:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__flores = np.empty(dimension, dtype=Flor)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregaFlor(self, flor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad] = flor
        self.__cantidad += 1

    def testFlores(self):
        with open("flores.csv") as file:
            reader = csv.reader(file, delimiter=";")
            next(file)
            for row in reader:
                flor = Flor(row[0], row[1], row[2], row[3])
                self.agregaFlor(flor)
        self.__flores.resize(self.__cantidad)

    def muestraFlores(self):
        for flor in self.__flores:
            print(flor)

    def getFlor(self, numero):
        flor = None
        if numero in range(1, len(self.__flores) + 1):
            flor = self.__flores[numero - 1]
        return flor

    def getLen(self):
        return len(self.__flores)

    def muestraCinco(self, lista):
        for i in range(len(lista)):
            print(self.getFlor(lista[i][0]))

