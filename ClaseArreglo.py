from zope.interface import implementer
from Interfaz import Interfaz
import numpy as np
from ClaseElemento import Elemento

@implementer(Interfaz)

class Arreglo:
    __dimension = 0
    __actual = 0
    __cantidad = 0
    __elementos = None

    def __init__(self, dimension = 10):
        self.__dimension = dimension
        self.__cantidad = 0
        self.__actual = 0
        self.__elementos = np.empty(dimension, dtype=Elemento)

    def insertarElemento(self, Elemento, posi):
        try:
            self.__elementos[posi] = Elemento
        except:
            print(f"la posicion {posi} no es valida")

    def agregarElemento(self, Elemento):
        self.__elementos[self.__actual] = Elemento
        self.__actual += 1

    def mostrarElemento(self, posi):
        try:
            print(self.__elementos[posi])
        except IndexError:
            print(f"la posicion {posi} no es valida para mostrar")