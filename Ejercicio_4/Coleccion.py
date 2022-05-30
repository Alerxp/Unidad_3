import csv, numpy as np
from Calefactor import Calefactor
from CalefactorElectrico import CalefactorElectrico
from CalefactorGas import CalefactorGas

class Coleccion:
    __actual = 0
    __dimension = 0
    __calefactores = None

    def __init__(self, dimension=10):
        self.__calefactores = np.empty(dimension, dtype=Calefactor)
        self.__actual = 0
        self.__dimension = dimension

    def agregaCalefactor(self, calefactor):
        self.__calefactores[self.__actual] = calefactor
        self.__actual += 1

    def testCalefactores(self):
        with open("calefactores-electricos.csv") as file:
            reader = csv.reader(file, delimiter=";")
            next(file)
            for row in reader:
                calefactor = CalefactorElectrico(row[0], row[1], row[2])
                self.agregaCalefactor(calefactor)

        with open("calefactores-gas.csv") as file:
            reader = csv.reader(file, delimiter=";")
            next(file)
            for row in reader:
                calefactor = CalefactorGas(row[0], row[1], row[2], row[3])
                self.agregaCalefactor(calefactor)

    def menorGas(self):
        aux, min = self.__calefactores[0], 9999
        for calefactor in self.__calefactores:
            if isinstance(calefactor, CalefactorGas) and calefactor.getCalorias() < min:
                aux = calefactor
                min = calefactor.getCalorias()
        return aux

    def menorElectrico(self):
        aux, min = self.__calefactores[0], 9999
        for calefactor in self.__calefactores:
            if isinstance(calefactor, CalefactorElectrico) and calefactor.getPotencia() < min:
                aux = calefactor
                min = calefactor.getPotencia()
        return aux

    def menorConsumo(self, kcal, kwatt):
        total_gas = self.menorGas().getCalorias() * kcal / 1000
        total_ele = self.menorElectrico().getPotencia() * kwatt / 1000
        if total_gas < total_ele:
            menor = self.menorGas()
        else:
            menor = self.menorElectrico()
        return menor

