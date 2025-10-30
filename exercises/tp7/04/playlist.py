from cancion import Cancion

class Playlist:
    def __init__(self, codigo:int, nombre:str):
        if not isinstance(codigo, int) or codigo < 0:
            raise ValueError("El codigo debe ser entero positivo")
        if not isinstance(nombre, str) or nombre.strip() == "" or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        
        self.__codigo = codigo
        self.__nombre = nombre
        self.__canciones = []


    def agregarCancion(self, cancion: "Cancion"):
        if not isinstance(cancion, Cancion):
            raise TypeError("Error")
        
        if not cancion in self.__canciones:
            self.__canciones.append(cancion)
        else:
            raise ValueError("La cancion ya esta en la playlist")
    
    def eliminarCancion(self, cancion: "Cancion"):
        if not isinstance(cancion, Cancion):
            raise TypeError("Error, la cancio debe ser valida")
    
        if cancion in self.__canciones:
            self.__canciones.remove(cancion)
        else:
            raise ValueError("La cancion no esta en la playlist")
        
    def obtenerCancion(self)->list:
        return self.__canciones