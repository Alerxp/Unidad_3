from os import system
from ObjectEncoder import ObjectEncoder
from IPersonal import IPersonal

def menu(lista):

    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("1. Insertar personal a la colección")
        print("2. Agregar personal a la colección")
        print("3. Tipo de personal en determinada posición")
        print("4. Listado de docentes investigadores en determinada carrera")
        print("5. Cantidad de inverstigadores en determinada área")
        print("6. Mostrar personal ordenado por apellido")
        print("7. Mostrar personal e importe extra en determinada categoría")
        print("8. Almacenar los datos de todo el personal en el archivo “personal.json”")
        print("0. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            personal = lista.creaPersonal()
            pos = int(input("Ingrese la posición [1, {}]: ".format(lista.getTope() + 1)))
            if pos < 1 or pos > lista.getTope() + 1:
                print("*** El número ingresado está fuera del intervalo ***")
            else:
                lista.insertarPersonal(personal, pos)
            system("pause")
        elif opc == 2:
            system("cls")
            personal = lista.creaPersonal()
            lista.agregarAlFinal(personal)
            system("pause")
        elif opc == 3:
            system("cls")
            pos = int(input("\nIngrese la posición [1, {}]: ".format(lista.getTope())))
            lista.muetraTipo(pos)
            system("pause")
        elif opc == 4:
            system("cls")
            carrera = input("\nNombre de carrera: ").upper()
            lista.muestraDocenteInvestigador(carrera)
            system("pause")
        elif opc == 5:
            system("cls")
            area = input("\nArea de investigación: ").title()
            lista.cuentaDocentesInvestigadores(area)
            system("pause")
        elif opc == 6:
            system("cls")
            lista.muestraAgentes()
            system("pause")
        elif opc == 7:
            system("cls")
            categoria = input("\nCategoría de investigación (I, II, III, IV o V): ").upper()
            lista.muestraImporteExtra(categoria)
            system("pause")
        elif opc == 8:
            system("cls")
            json.guardarJSONArchivo(lista.toJSON(), "personal.json")
            system("pause")
        elif opc == 0:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    json = ObjectEncoder()
    diccionario = json.leerJSONArchivo("personal.json")
    lista = json.decodificarDiccionario(diccionario)
    menu(IPersonal(lista))
