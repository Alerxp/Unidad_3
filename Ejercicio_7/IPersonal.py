from zope.interface import Interface

class IPersonal(Interface):
    def insertarPersonal(personal, posicion):
        pass

    def agregarPersonal(personal):
        pass

    def muestraTipo(posicion):
        pass
