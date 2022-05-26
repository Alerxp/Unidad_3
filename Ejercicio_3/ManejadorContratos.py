import csv, numpy as np
from claseContrato import Contrato

class ManejadorContratos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__contratos = np.empty(dimension, dtype=Contrato)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregaContrato(self, contrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__contratos.resize(self.__dimension)
        self.__contratos[self.__cantidad] = contrato
        self.__cantidad += 1

    def muestraContratado(self, dni):
        i = 0
        while i < self.__cantidad and self.__contratos[i].getJugador().getDNI() != dni:
            i += 1
        if i < self.__cantidad:
            print(f"\nNombre del equipo: {self.__contratos[i].getEquipo().getNombre()}")
            print(f"Fecha de finalización del contrato: {self.__contratos[i].getFechaFin()}")
        else:
            print("\nEl DNI ingresado no corresponde a un jugador contratado")

    def guardaContratos(self):
        with open("Contratos.csv", "w", newline="") as file:
            writer = csv.writer(file)
            contratos = [["DNI", "Equipo", "Fecha de inicio", "Fecha de fin", "Pago mensual"]]
            for i in range(self.__cantidad):
                dni = self.__contratos[i].getJugador().getDNI()
                equipo = self.__contratos[i].getEquipo().getNombre()
                inicio = self.__contratos[i].getFechaInicio()
                fin = self.__contratos[i].getFechaFin()
                pago = self.__contratos[i].getPago()
                fila = [dni, equipo, inicio, fin, pago]
                contratos.append(fila)
            writer.writerows(contratos)
        print("\n*** Los contratos se almacenaron exitosamente ***")

