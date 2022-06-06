from zope.interface import Interface

class IPersonal(Interface):
    def insertarPersonal(self, personal, posicion):
        pass

    def agregarPersonal(self, personal):
        pass

    def muestraTipo(self, posicion):
        pass
