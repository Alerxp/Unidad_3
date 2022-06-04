from zope.interface import Interface

class IAparato(Interface):
    def insertarAparato(self, aparato, posicion):
        pass

    def agregarAparato(self, aparato):
        pass

    def muestraTipo(self, posicion):
        pass
