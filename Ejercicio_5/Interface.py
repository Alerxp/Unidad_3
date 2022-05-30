from zope.interface import Interface, implementer

class Coleccion(Interface):
    def insertarElemento(elemento, posicion):
        pass

    def agregarElemento(elemento):
        pass

    def mostrarElemento(posicion):
        pass
