from Nodo import Nodo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from Apoyo import Apoyo
from zope.interface import implementer
from IPersonal import IPersonal
from ITesorero import ITesorero
from IDirector import IDirector

@implementer(IPersonal)
@implementer(ITesorero)
@implementer(IDirector)
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

    def agregarPersonal(self, personal):    # Agrega por la cabeza
        nodo = Nodo(personal)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def agregarAlFinal(self, personal):
        if self.__comienzo is None:
            self.agregarPersonal(personal)
        else:
            nodo = Nodo(personal)
            nodo.setSiguiente(None)
            aux, anterior = self.__comienzo, None
            while aux is not None:
                anterior = aux
                aux = aux.getSiguiente()
            anterior.setSiguiente(nodo)
            self.__tope += 1

    def insertarPersonal(self, personal, posicion):
        if posicion == 1:
            self.agregarPersonal(personal)
        elif posicion == self.__tope + 1:
            self.agregarAlFinal(personal)
        else:
            nodo = Nodo(personal)
            anterior, aux = self.__comienzo, self.__comienzo.getSiguiente()
            indice = 2
            while indice != posicion:
                anterior = aux
                aux = aux.getSiguiente()
                indice += 1
            anterior.setSiguiente(nodo)
            nodo.setSiguiente(aux)
            self.__tope += 1

    def creaPersonal(self):
        print("\n=== DATOS PERSONALES ===")
        cuil = input("CUIL: ")
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        basico = int(input("Sueldo b??sico: "))
        antiguedad = int(input("Antig??edad: "))
        tipo = input("\nSeleccione tipo de personal (1.Docente, 2.Investigador, 3.Docente Investigador, 4.Apoyo): ")
        while tipo not in ["1", "2", "3", "4"]:
            print("El dato ingresado no es correcto")
            tipo = input("Seleccione tipo de personal (1.Docente, 2.Investigador, 3.Docente Investigador, 4.Apoyo): ")
        personal = None
        if tipo == "1":
            carrera = input("Carrera: ")
            cargo = input("Cargo: ")
            catedra = input("C??tedra: ")
            personal = Docente(cuil, apellido, nombre, basico, antiguedad, "", "", carrera, cargo, catedra)
        elif tipo == "2":
            area = input("Area de investigaci??n: ")
            tipo = input("Tipo de investigaci??n: ")
            personal = Investigador(cuil, apellido, nombre, basico, antiguedad, area, tipo, "", "", "")
        elif tipo == "3":
            area = input("Area de investigaci??n: ")
            tipo = input("Tipo de investigaci??n: ")
            carrera = input("Carrera: ")
            cargo = input("Cargo: ")
            catedra = input("C??tedra: ")
            categoria = input("Categor??a: ")
            importe = int(input("Importe extra: "))
            personal = DocenteInvestigador(cuil, apellido, nombre, basico, antiguedad, area, tipo, carrera, cargo, catedra, categoria, importe)
        elif tipo == "4":
            categoria = input("Categor??a: ")
            personal = Apoyo(cuil, apellido, nombre, basico, antiguedad, categoria)
        return personal

    def muetraTipo(self, posicion):
        aux, indice = self.__comienzo, 1
        while indice != posicion and aux is not None:
            aux = aux.getSiguiente()
            indice += 1
        if aux is None:
            print("*** El n??mero ingresado est?? fuera del intervalo ***")
        else:
            tipo = type(aux.getDato()).__name__
            print("Tipo de agente: {}".
                  format("Docente Investigador" if tipo == "DocenteInvestigador" else tipo))

    def muestraDocenteInvestigador(self, carrera):
        di = []
        for personal in self:
            if isinstance(personal, DocenteInvestigador):
                if personal.getCarrera() == carrera:
                    di.append(personal)

        if len(di) == 0:
            print("No hay Docentes Investigadores en {}".format(carrera))
        else:
            di.sort()
            print("=== DOCENTES INVESTIGADORES DE {} ===".format(carrera))
            for personal in di:
                personal.mostrarDatos()
                print("-----------------------------------")

    def cuentaDocentesInvestigadores(self, area):
        i, di = 0, 0
        for personal in self:
            if type(personal) == Investigador and personal.getArea() == area:
                i += 1
            elif type(personal) == DocenteInvestigador and personal.getArea() == area:
                di += 1
        print("=== AREA DE INVESTIGACION {} ===".format(area.upper()))
        print("Cantidad de investigadores: {}\nCantidad de Docentes Investigadores: {}".
              format(i, di))

    def muestraAgentes(self):
        p = []
        for personal in self:
            p.append(personal)

        p.sort()
        print("\n| APELLIDO | NOMBRE |   TIPO DE AGENTE   | SUELDO |")
        for personal in p:
            tipo = type(personal).__name__
            print("|{:<10}|{:<8}|{:<20}|${:>7}|".format(personal.getApellido(), personal.getNombre(),
                                                     "Docente Investigador" if tipo == "DocenteInvestigador" else tipo,
                                                     personal.getSueldo()))

    def muestraImporteExtra(self, categoria):
        if categoria not in ["I", "II", "III", "IV", "V"]:
            print("*** La categor??a no es v??lida ***")
        else:
            print("\n| APELLIDO | NOMBRE | EXTRA |")
            acum = 0
            for personal in self:
                if isinstance(personal, DocenteInvestigador) and personal.getCategoria() == categoria:
                    acum += personal.getImporte()
                    print("|{:<10}|{:<8}|${:>6}|".format(personal.getApellido(), personal.getNombre(), personal.getImporte()))
            print(f"\nTotal de importes extra: ${acum}")

    def tipoDeUsuario(self):
        u = None
        user = input("Usuario: ")
        password = input("Contrase??a: ")
        if user == "uTesorero" and password == "ag@74ck":
            u = "tesorero"
        elif user == "uDirector" and password == "ufC77#!1":
            u = "director"
        return u

    def gastosSueldoPorEmpleado(self, cuil):
        aux = self.__comienzo
        while aux is not None and aux.getDato().getCuil() != cuil:
            aux = aux.getSiguiente()
        if aux is not None:
            print(f"Sueldo del agente ${aux.getDato().getSueldo()}")
        else:
            print("El CUIL ingresado no corresponde a ning??n agente")

    def buscaAgente(self, cuil):
        aux, agente = self.__comienzo, None
        while aux is not None and aux.getDato().getCuil() != cuil:
            aux = aux.getSiguiente()
        if aux is not None:
            agente = aux.getDato()
        return agente

    def modificarBasico(self, cuil, nuevoBasico):
        agente = self.buscaAgente(cuil)
        if agente:
            agente.setBasico(nuevoBasico)
        else:
            print("El CUIL ingresado no corresponde a ning??n agente")

    def modificarCargo(self, cuil, nuevoCargo):
        agente = self.buscaAgente(cuil)
        if agente:
            agente.setCargo(nuevoCargo)
        else:
            print("El CUIL ingresado no corresponde a ning??n agente")

    def modificarCategoria(self, cuil, nuevaCategoria):
        agente = self.buscaAgente(cuil)
        if agente:
            agente.setCategoria(nuevaCategoria)
        else:
            print("El CUIL ingresado no corresponde a ning??n agente")

    def modificarImporteExtra(self, cuil, nuevoImporteExtra):
        agente = self.buscaAgente(cuil)
        if agente:
            agente.setImporte(nuevoImporteExtra)
        else:
            print("El CUIL ingresado no corresponde a ning??n agente")

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            datos=[personal.toJSON() for personal in self]
        )
        return d
