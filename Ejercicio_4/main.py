from os import system
from Coleccion import Coleccion
from CalefactorGas import CalefactorGas

def menu():

    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("1. Calefactor a gas de menor consumo")
        print("2. Calefactor eléctrico de menor consumo")
        print("3. Calefactor de menor consumo")
        print("0. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            print(f"\nMarca: {coleccion.menorGas().getMarca()} - Modelo: {coleccion.menorGas().getmodelo()}")
            system("pause")
        elif opc == 2:
            system("cls")
            print(f"\nMarca: {coleccion.menorElectrico().getMarca()} - Modelo: {coleccion.menorElectrico().getmodelo()}")
            system("pause")
        elif opc == 3:
            system("cls")
            kcal = float(input("\nIngrese el precio de la kcal/h: "))
            kwatt = float(input("Ingrese el precio del kilowatt/h: "))
            menor = coleccion.menorConsumo(kcal, kwatt)
            print("\nTipo: Calefactor {} - {}".format("a Gas" if isinstance(menor, CalefactorGas) else "eléctrico", menor))
            system("pause")
        elif opc == 0:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    print("************ BIENVENIDO ************\n")
    flag, cantidad = True, 0
    while flag:
        try:
            cantidad = int(input("Ingrese la cantidad de calefactores: "))
            if cantidad > 0:
                flag = False
            else:
                print("\nLa cantidad no puede ser un número menor o igual a 0")
        except:
            print("\nSólo puede ingresar números")

    coleccion = Coleccion(cantidad)
    coleccion.testCalefactores()
    menu()
