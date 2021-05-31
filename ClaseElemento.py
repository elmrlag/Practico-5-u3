class Elemento:
    __edad = 0
    __nombre = 0

    def __init__(self, v1,v2):
        self.__edad = v1
        self.__nombre = v2

    def __str__(self):
        cadena = f"Edad: {self.__edad} -- Nombre: {self.__nombre}"
        return cadena