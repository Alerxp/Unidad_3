from Nodo import Nodo
from Televisor import Televisor
from Heladera import Heladera
from Lavarropas import Lavarropas
from zope.interface import implementer
from IAparato import IAparato

@implementer(IAparato)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def getTope(self):
        return self.__tope

    def agregarAparato(self, aparato):    # Agrega por la cabeza
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def agregarAlFinal(self, aparato):
        if self.__comienzo is None:
            self.agregarAparato(aparato)
        else:
            nodo = Nodo(aparato)
            nodo.setSiguiente(None)
            aux, anterior = self.__comienzo, None
            while aux is not None:
                anterior = aux
                aux = aux.getSiguiente()
            anterior.setSiguiente(nodo)
            self.__tope += 1

    def insertarAparato(self, aparato, posicion):
        if posicion == 1:
            self.agregarAparato(aparato)
        elif posicion == self.__tope + 1:
            self.agregarAlFinal(aparato)
        else:
            nodo = Nodo(aparato)
            anterior, aux = self.__comienzo, self.__comienzo.getSiguiente()
            indice = 2
            while indice != posicion:
                anterior = aux
                aux = aux.getSiguiente()
                indice += 1
            anterior.setSiguiente(nodo)
            nodo.setSiguiente(aux)
            self.__tope += 1

    def muetraTipo(self, posicion):
        aux, indice = self.__comienzo, 1
        while indice != posicion and aux is not None:
            aux = aux.getSiguiente()
            indice += 1
        if aux is None:
            print("*** El número ingresado está fuera del intervalo ***")
        else:
            tipo = type(aux.getDato()).__name__
            print("En la posición ingresada hay un{}: {}".format("a" if tipo == "Heladera" else "", tipo))

    def cuentaPhillips(self):
        t, h, l, aux = 0, 0, 0, self.__comienzo
        while aux is not None:
            if aux.getDato().getMarca() == "Philips":
                if isinstance(aux.getDato(), Televisor):
                    t += 1
                elif isinstance(aux.getDato(), Heladera):
                    h += 1
                elif isinstance(aux.getDato(), Lavarropas):
                    l += 1
            aux = aux.getSiguiente()
        return t, h, l

    def marcaCargaSuperior(self):
        aux = self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), Lavarropas):
                if aux.getDato().getCarga() == "Superior":
                    print(aux.getDato().getMarca())
            aux = aux.getSiguiente()

    def mostrarAparatos(self):
        print("\n| PRODUCTO | MARCA | ORIGEN  | IMPORTE |")
        for aparato in self:
            print("|{:<10}|{:<7}|{}|${:>8}|".format(aparato.__class__.__name__, aparato.getMarca(), aparato.getOrigen(), aparato.importeVenta()))

    def creaAparato(self):
        print("\n=== DATOS DEL APARATO ===")
        tipo = input("Ingrese tipo de aparato (Televisor, Heladera, Lavarropas): ").lower()
        while tipo not in ["televisor", "heladera", "lavarropas"]:
            print("El dato ingresado no es correcto")
            tipo = input("Ingrese tipo de aparato (Televisor, Heladera, Lavarropas): ").lower()
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        origen = input("País de fabricación: ")
        base = int(input("Precio base: "))
        aparato = None
        if tipo == "televisor":
            pantalla = input("Tipo de pantalla: ")
            pulgadas = int(input("Tamaño en pulgadas: "))
            definicion = input("Resolución: ")
            internet = True if input("Internet (s/n): ").lower() == "s" else False
            aparato = Televisor(marca, modelo, color, origen, base, pantalla, pulgadas, definicion, internet)
        elif tipo == "heladera":
            capacidad = int(input("Capacidad el litros: "))
            freezer = True if input("Freezer (s/n): ").lower() == "s" else False
            ciclica = True if input("Cíclica (s/n): ").lower() == "s" else False
            aparato = Heladera(marca, modelo, color, origen, base, capacidad, freezer, ciclica)
        elif tipo == "lavarropas":
            capacidad = int(input("Capacidad en kg: "))
            rpm = int(input("Velocidad de centrifugado en rpm: "))
            programas = int(input("Cantidad de programas: "))
            carga = input("Tipo de carga (Frontal/Superior): ")
            aparato = Lavarropas(marca, modelo, color, origen, base, capacidad, rpm, programas, carga)
        return aparato

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            datos=[aparato.toJSON() for aparato in self]
        )
        return d
