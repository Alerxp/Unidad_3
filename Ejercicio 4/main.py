from os import system
from ListaSecuencial import Lista

if __name__ == '__main__':
    designaciones = Lista(3)
    designaciones.testArchivo()
    cargo = input("Ingrese tipo de cargo (Defensor, Fiscal, Juez): ").title()
    designaciones.cargoMujeres(cargo)
    system('pause')
    system('cls')
    materia = input("Ingrese materia (Penal, Múltiple, Electoral, Seguridad social, etc): ").title()
    cargo = input("Ingrese tipo de cargo (Defensor, Fiscal, Juez): ").title()
    anio = int(input("Año entre 2000 y 2021: "))
    cant = designaciones.cantidadAgentes(materia, cargo, anio)
    if cant:
        print(f"Cantidad de agentes designados en materia {materia}, cargo {cargo}, año {anio}: {cant}")
    else:
        print("No hubieron agentes designados")
