from os import system
from ManejadorEquipos import ManejadorEquipo
from ManejadorJugadores import ManejadorJugadores
from ManejadorContratos import ManejadorContratos
from claseJugador import Jugador
from claseContrato import Contrato

def menu():

    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("1. Crear contrato")
        print("2. Consultar jugadores contratados")
        print("3. Consultar contratos que vencen en 6 meses")
        print("4. Obtener importe de contratos")
        print("5. Guardar contratos")
        print("0. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            print("\n=== DATOS DEL JUGADOR ===")
            nom = input("Nombre: ")
            dni = input("DNI: ")
            ciudad = input("Ciudad Natal: ")
            pais = input("País de origen: ")
            fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
            jugador = Jugador(nom, dni, ciudad, pais, fecha)    # instancia de la clase Jugador
            manejaJugadores.agregaJugador(jugador)    # agrega el jugador a la lista
            nom_equipo = input("Nombre del equipo: ").lower()
            equipo = manejaEquipos.buscaEquipo(nom_equipo)    # instancia de la clase Equipo
            while not equipo:
                print("*** EL NOMBRE NO ES CORRECTO ***")
                nom_equipo = input("Ingrese nuevamente el nombre del equipo: ").lower()
                equipo = manejaEquipos.buscaEquipo(nom_equipo)
            print("=== DATOS DEL CONTRATO ===")
            inicio = input("Fecha de inicio (dd/mm/aaaa): ")
            fin = input("Fecha de finalización (dd/mm/aaaa): ")
            pago = int(input("Pago mensual: "))
            contrato = Contrato(inicio, fin, pago, jugador, equipo)    # instancia de la clase Contrato
            manejaContratos.agregaContrato(contrato)    # agrega el contrato al array
            equipo.agregaContrato(contrato)    # agrega el contrato a la lista del equipo
            system("pause")
        elif opc == 2:
            system("cls")
            dni = input("\nIngrese DNI del jugador: ")
            manejaContratos.muestraContratado(dni)
            system("pause")
        elif opc == 3:
            system("cls")
            nom_equipo = input("\nNombre del equipo: ").lower()
            manejaEquipos.contratosQueVencen(nom_equipo)
            system("pause")
        elif opc == 4:
            system("cls")
            nom_equipo = input("\nNombre del equipo: ").lower()
            importe = manejaEquipos.importeContratos(nom_equipo)
            if importe:
                print(f"\nEl importe total de los contratos del equipo es: ${importe}")
            else:
                print("\nEl equipo no tiene contratos")
            system("pause")
        elif opc == 5:
            system("cls")
            manejaContratos.guardaContratos()
            system("pause")
        elif opc == 0:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    manejaEquipos = ManejadorEquipo(3)
    manejaEquipos.testEquipos()
    manejaJugadores = ManejadorJugadores()
    manejaContratos = ManejadorContratos(1)
    menu()
