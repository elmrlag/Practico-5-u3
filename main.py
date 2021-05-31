from ClaseElemento import Elemento
from ClaseArreglo import Arreglo

def Testeo():
    print("se inicia el testeo")
    UnElemento = Elemento(10, "Adriel")
    OtroElemento = Elemento(25, "Adriel2")
    MArreglo.agregarElemento(UnElemento)
    MArreglo.agregarElemento(OtroElemento)

    MArreglo.mostrarElemento(14)
    MArreglo.mostrarElemento(0)
    MArreglo.mostrarElemento(1)

    MArreglo.insertarElemento(OtroElemento, 34)
    MArreglo.insertarElemento(OtroElemento, 8)
    MArreglo.mostrarElemento(8)


if __name__=='__main__':
    MArreglo = Arreglo()
    Testeo()