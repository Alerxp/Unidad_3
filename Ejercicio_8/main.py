from os import system
from ObjectEncoder import ObjectEncoder
from IPersonal import IPersonal
from ITesorero import ITesorero
from IDirector import IDirector

def menuDirector(lista):
    while True:
        print("************************* OPCIONES DE DIRECTOR *************************")
        print(" 1. Modificar sueldo básico")
        print(" 2. Modificar cargo")
        print(" 3. Modificar categoría")
        print(" 4. Modificar importe extra")
        print(" 0. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            cuil = input("\nIngrese CUIL del agente: ")
            basico = input("Ingrese nuevo sueldo básico: ")
            lista.modificarBasico(cuil, basico)
            system("pause")
        elif opc == 2:
            system("cls")
            cuil = input("\nIngrese CUIL del agente: ")
            cargo = input("Ingrese nuevo cargo: ")
            while cargo not in ["simple", "semiexclusivo", "exclusivo"]:
                print("*** ERROR ***")
                cargo = input("Ingrese el nuevo cargo: ")
            lista.modificarCargo(cuil, cargo)
            system("pause")
        elif opc == 3:
            system("cls")
            cuil = input("\nIngrese CUIL del agente: ")
            categoria = int(input("Ingrese nueva categoría [1, 22]: "))
            while categoria not in range(1, 23):
                print("*** ERROR ***")
                categoria = int(input("Ingrese nueva categoría [1, 22]: "))
            lista.modificarCategoria(cuil, categoria)
            system("pause")
        elif opc == 4:
            system("cls")
            cuil = input("\nIngrese CUIL del agente: ")
            importe = int(input("Ingrese nuevo importe extra: "))
            while importe <= 0:
                print("*** ERROR ***")
                importe = int(input("Ingrese nuevo importe extra: "))
            lista.modificarImporteExtra(cuil, importe)
            system("pause")
        elif opc == 0:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

def menu(lista):

    while True:
        print("*************************** MENÚ DE OPCIONES ***************************")
        print(" 1. Insertar personal a la colección")
        print(" 2. Agregar personal a la colección")
        print(" 3. Tipo de personal en determinada posición")
        print(" 4. Listado de docentes investigadores en determinada carrera")
        print(" 5. Cantidad de investigadores en determinada área")
        print(" 6. Mostrar personal ordenado por apellido")
        print(" 7. Mostrar personal e importe extra en determinada categoría")
        print(" 8. Almacenar los datos de todo el personal en el archivo “personal.json”")
        print("****************** OPCIONES PARA TESORERO Y DIRECTOR *******************")
        print(" 9. Consultar sueldo de empleado (Tesorero)")
        print("10. Menú de opciones (Director)")
        print(" 0. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            personal = list.creaPersonal()
            pos = int(input("Ingrese la posición [1, {}]: ".format(lista.getTope() + 1)))
            if pos < 1 or pos > list.getTope() + 1:
                print("*** El número ingresado está fuera del intervalo ***")
            else:
                lista.insertarPersonal(personal, pos)
            system("pause")
        elif opc == 2:
            system("cls")
            personal = list.creaPersonal()
            list.agregarAlFinal(personal)
            system("pause")
        elif opc == 3:
            system("cls")
            pos = int(input("\nIngrese la posición [1, {}]: ".format(lista.getTope())))
            lista.muetraTipo(pos)
            system("pause")
        elif opc == 4:
            system("cls")
            carrera = input("\nNombre de carrera: ").upper()
            list.muestraDocenteInvestigador(carrera)
            system("pause")
        elif opc == 5:
            system("cls")
            area = input("\nArea de investigación: ").title()
            list.cuentaDocentesInvestigadores(area)
            system("pause")
        elif opc == 6:
            system("cls")
            list.muestraAgentes()
            system("pause")
        elif opc == 7:
            system("cls")
            categoria = input("\nCategoría de investigación (I, II, III, IV o V): ").upper()
            list.muestraImporteExtra(categoria)
            system("pause")
        elif opc == 8:
            system("cls")
            json.guardarJSONArchivo(list.toJSON(), "personal.json")
            system("pause")
        elif opc == 9:
            system("cls")
            if list.tipoDeUsuario() == "tesorero":
                cuil = input("\nIngrese CUIL del agente: ")
                listaT = ITesorero(list)
                listaT.gastosSueldoPorEmpleado(cuil)
            else:
                print("*** Error de Usuario/Contraseña ***")
            system("pause")
        elif opc == 10:
            system("cls")
            if list.tipoDeUsuario() == "director":
                system("cls")
                listaD = IDirector(list)
                menuDirector(listaD)
            else:
                print("*** Error de Usuario/Contraseña ***")
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
    list = json.decodificarDiccionario(diccionario)
    menu(IPersonal(list))
