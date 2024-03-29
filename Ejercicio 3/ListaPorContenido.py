import csv
from Nodo import Nodo
from Provincia import Provincia

class Lista:
    __cabeza = None
    __cantidad = 0

    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0

    def testArchivo(self):
        with open('superficie-afectada-por-incendios.csv') as file:
            reader = csv.reader(file, delimiter=';')
            next(file)
            acum = 0
            ant = None
            for row in reader:
                prov = row[3]
                if ant is not None and ant != prov:
                    self.insertar(Provincia(ant, acum))
                    acum = 0
                if row[6] != '':
                    acum += float(row[6])
                ant = prov

    def vacia(self):
        return self.__cantidad == 0

    def insertar(self, x):  # de mayor a menor
        if isinstance(x, Provincia):
            if self.vacia():
                nodo = Nodo(x)
                self.__cabeza = nodo
            else:
                if x > self.__cabeza.getDato():
                    nodo = Nodo(x)
                    nodo.setSiguiente(self.__cabeza)
                    self.__cabeza = nodo
                else:
                    aux = self.__cabeza
                    sig = aux.getSiguiente()
                    while sig is not None and x <= sig.getDato():
                        aux = sig
                        sig = sig.getSiguiente()
                    nodo = Nodo(x)
                    aux.setSiguiente(nodo)
                    nodo.setSiguiente(sig)
            self.__cantidad += 1

    def suprmir(self, p):
        if self.vacia():
            print("Lista vacía")
        else:
            if p in range(1, self.__cantidad+1):
                if p == 1:
                    self.__cabeza = self.__cabeza.getSiguiente()
                else:
                    aux = self.__cabeza
                    sig = aux.getSiguiente()
                    pos = 1
                    while pos != p-1:
                        aux = sig
                        sig = sig.getSiguiente()
                        pos += 1
                    aux.setSiguiente(sig.getSiguiente())
                self.__cantidad -= 1
            else:
                print(f"Error: rango de posiciones disponibles [1, {self.__cantidad}]")

    def recuperar(self, p):
        if self.vacia():
            print("Lista vacía")
        else:
            if p in range(1, self.__cantidad+1):
                if p == 1:
                    return self.__cabeza.getDato()
                else:
                    aux = self.__cabeza
                    pos = 1
                    while pos != p:
                        aux = aux.getSiguiente()
                        pos += 1
                    return aux.getDato()
            else:
                print(f"Error: rango de posiciones disponibles [1, {self.__cantidad}]")

    def buscar(self, x):
        if not self.vacia():
            p = None
            pos = 1
            aux = self.__cabeza
            while aux is not None and aux.getDato() != x:
                aux = aux.getSiguiente()
                pos += 1
            if pos <= self.__cantidad:
                p = pos
            return p

    def primero(self):
        if not self.vacia():
            return self.__cabeza.getDato()

    def ultimo(self):
        if not self.vacia():
            aux = self.__cabeza
            while aux.getSiguiente() is not None:
                aux = aux.getSiguiente()
            return aux.getDato()

    def recorrer(self):
        print("+-------------------+-------------------------------+")
        print("|     Provincia     |   Superficie Total Afectada   |")
        print("+-------------------+-------------------------------+")
        aux = self.__cabeza
        while aux is not None:
            provincia = aux.getDato()
            print("|{:<19}|{:>31}|".format(provincia.getNombre(), round(provincia.getSuperficie(), 1)))
            aux = aux.getSiguiente()
        print("+-------------------+-------------------------------+")
