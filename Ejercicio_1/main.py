from os import system
from ManejaFacultades import ManejaFacultades

def menu():

    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("1. Ver carreras de una facultad")
        print("2. Lugar de cursado de una carrera")
        print("3. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            cod = int(input("\nIngrese el código de una facultad: "))
            if cod:
                manejaFacu.muestraFacultad(cod)
            else:
                print("\nEl código ingresado no es correcto\n")
            system("pause")
        elif opc == 2:
            system("cls")
            nom = input("\nIngrese un nombre de carrea: ")
            datos = manejaFacu.buscaNombre(nom.lower())    # string con los datos o None
            print("{}\n".format(datos if datos else "El nombre ingresado no es correcto"))
            system("pause")
        elif opc == 3:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    manejaFacu = ManejaFacultades()
    manejaFacu.testFacultades()
    menu()
