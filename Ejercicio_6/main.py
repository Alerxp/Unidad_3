from os import system
from ObjectEncoder import ObjectEncoder
from IAparato import IAparato

def menu():

    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("1. Insertar un aparato en la colección en una posición determinada")
        print("2. Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan)")
        print("3. Dada una posición de la Lista, mostrar qué tipo de objeto se encuentra almacenado en dicha posición")
        print("4. Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea Phillips")
        print("5. Mostrar la marca de todos los lavarropas que tienen carga superior")
        print("6. Mostrar de todos los aparatos, marca, país de fabricación e importe de venta")
        print("7. Almacenar los objetos de la colección Lista en el archivo 'aparatoselectronicos.json'")
        print("0. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            aparato = lista.creaAparato()
            pos = int(input("Ingrese la posición [1, {}]: ".format(lista.getTope() + 1)))
            if pos < 1 or pos > lista.getTope() + 1:
                print("*** El número ingresado está fuera del intervalo ***")
            else:
                lista.insertarAparato(aparato, pos)
            system("pause")
        elif opc == 2:
            system("cls")
            aparato = lista.creaAparato()
            lista.agregarAlFinal(aparato)
            system("pause")
        elif opc == 3:
            system("cls")
            pos = int(input("Ingrese la posición [1, {}]: ".format(lista.getTope())))
            lista.muetraTipo(pos)
            system("pause")
        elif opc == 4:
            system("cls")
            phillips = lista.cuentaPhillips()
            print("\n=== PHILIPS ===")
            print("Televisores: {:>2}\nHeladeras: {:>4}\nLavarropas: {:>3}".
                  format(phillips[0], phillips[1], phillips[2]))
            system("pause")
        elif opc == 5:
            system("cls")
            print("\n=== MARCAS LAVARROPAS CARGA SUPERIOR ===")
            lista.marcaCargaSuperior()
            system("pause")
        elif opc == 6:
            system("cls")
            lista.mostrarAparatos()
            system("pause")
        elif opc == 7:
            system("cls")
            json.guardarJSONArchivo(lista.toJSON(), "aparatoselectronicos.json")
            system("pause")
        elif opc == 0:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    json = ObjectEncoder()
    diccionario = json.leerJSONArchivo("aparatoselectronicos.json")
    lista = IAparato(json.decodificarDiccionario(diccionario))
    menu()
