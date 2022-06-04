import json
from pathlib import Path
from Lista import Lista
from Televisor import Televisor
from Heladera import Heladera
from Lavarropas import Lavarropas

class ObjectEncoder:
    def decodificarDiccionario(self, d):
        if "__class__" not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == "Lista":
                elementos = d["datos"]
                lista = class_()
                for i in range(len(elementos)):
                    dElemento = elementos[i]
                    class_name = dElemento.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dElemento['__atributos__']
                    unAparato = class_(**atributos)
                    #lista.agregarAparato(unAparato)
                    lista.agregarAlFinal(unAparato)
                return lista

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            return diccionario
