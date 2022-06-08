from zope.interface import Interface

class IAparato(Interface):
    def insertarAparato(aparato, posicion):
        pass

    def agregarAparato(aparato):
        pass

    def muestraTipo(posicion):
        pass
