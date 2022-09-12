import numpy as np

class Lista:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__lista = np.empty(dimension, dtype=int)
        self.__cantidad = 0
        self.__dimension = dimension

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
                self.__lista[p-1] = x
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
            while i < self.__cantidad and self.__lista[i] != x:
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

    def siguiente(self, p):
        if not self.vacia():
            if p in range(1, self.__cantidad):
                return hex(id(self.__lista[p]))
            else:
                print("Error de posición")
        else:
            print("Lista vacía")

    def anterior(self, p):
        if not self.vacia():
            if p in range(2, self.__cantidad+1):
                return hex(id(self.__lista[p-2]))
            else:
                print("Error de posición")
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
