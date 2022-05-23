from claseRamo import Ramo

class ManejaRamos:
    __ventas = []

    def __init__(self):
        self.__ventas = []

    def registraVenta(self, ramo):
        if isinstance(ramo, Ramo):
            self.__ventas.append(ramo)

    def muestraPorTamano(self, tamano):
        for ramo in self.__ventas:
            if ramo.getTamano() == tamano:
                print(ramo)

    def getVentas(self):
        return self.__ventas

    def cincoMas(self, flores):
        from operator import itemgetter
        # count = [[número de flor, cantidad pedida], [..., ...], [..., ...], ...]
        count = [[i + 1, 0] for i in range(flores.getLen())]
        for ramo in self.__ventas:
            for flor in ramo.getFlores():
                count[flor.getNumero() - 1][1] += 1
        # orden descendente conciderando cantidad pedida
        count.sort(key=itemgetter(1), reverse=True)
        count = count[:5]    # sólo guardo las cinco primeraas
        return count

