from zope.interface import Interface

class IDirector(Interface):
    def modificarBasico(cuil, nuevoBasico):
        pass

    def modificarCargo(cuil, nuevoCargo):
        pass

    def modificarCategoria(cuil, nuevaCategoria):
        pass

    def modificarImporteExtra(cuil, nuevoImporteExtra):
        pass
