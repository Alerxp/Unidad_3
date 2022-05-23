from os import system
from claseRamo import Ramo
from ManejaFlores import ManejaFlores
from ManejaRamos import ManejaRamos

def menu():

    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("1. Registrar venta")
        print("2. Mostrar las 5 flores mas pedidas")
        print("3. Mostrar flores vendidas según tamaño de ramo")
        print("0. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            print("\n===== VENTA =====\n")
            tamano = input("Ingrese el tamaño del ramo (chico/mediano/grande): ").lower()
            while tamano not in ["chico", "mediano", "grande"]:
                print("\nOPCIÓN INCORRECTA\n")
                tamano = input("Ingrese el tamaño del ramo (chico/mediano/grande): ")
            print("\n*** Puede elegir hasta 4 tipos de flores para el ramo ***")
            system("pause")
            manejaFlores.muestraFlores()
            numero = input("\nSeleccione una flor (presione 0 para terminar): ")
            flores = []    # referencias a instancias de la clase Flor
            while numero != "0" and len(flores) < 4:
                if manejaFlores.getFlor(int(numero)):
                    if manejaFlores.getFlor(int(numero)) in flores:
                        print(f"Ya seleccionó la {manejaFlores.getFlor(int(numero))}")
                    else:
                        print(manejaFlores.getFlor(int(numero)))
                        flores.append(manejaFlores.getFlor(int(numero)))
                else:
                    print("\nOPCIÓN INCORRECTA")
                if len(flores) < 4:
                    numero = input("\nSeleccione una flor (presione 0 para terminar): ")
                else:
                    numero = "0"
            if len(flores) > 0:
                unRamo = Ramo(tamano, flores)
                manejaRamos.registraVenta(unRamo)
                print(unRamo)
            system("pause")
        elif opc == 2:
            system("cls")
            if manejaRamos.getVentas():
                print("\n===== Las 5 flores mas pedidas son =====:\n")
                manejaFlores.muestraCinco(manejaRamos.cincoMas(manejaFlores))
            else:
                print("*** No hay ventas registradas ***")
            system("pause")
        elif opc == 3:
            system("cls")
            if manejaRamos.getVentas():
                tamano = input("\nIngrese el tamaño del ramo (chico/mediano/grande): ").lower()
                while tamano not in ["chico", "mediano", "grande"]:
                    print("\nOPCIÓN INCORRECTA\n")
                    tamano = input("Ingrese el tamaño del ramo (chico/mediano/grande): ").lower()
                manejaRamos.muestraPorTamano(tamano)
            else:
                print("*** No hay ventas registradas ***")
            system("pause")
        elif opc == 0:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    manejaFlores = ManejaFlores(3)
    manejaFlores.testFlores()
    manejaRamos = ManejaRamos()
    menu()
