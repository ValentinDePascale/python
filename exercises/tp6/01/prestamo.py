from libro import Libro
from fecha import Fecha
from socios import Socio

class Prestamo:
    def __init__(self, libro:Libro, socio:Socio, fechaPrestamo:Fecha, dias:int):


        if not isinstance(libro, Libro):
            raise ValueError("Error")
        if not isinstance(socio, Socio):
            raise ValueError("Error")
        if not isinstance(fechaPrestamo, Fecha):
            raise ValueError("Error")
        if not isinstance(dias, int):
            raise ValueError("Error")

        self.__libro = libro
        self.__socio = socio
        self.__fechaPrestamo = fechaPrestamo
        self.__cantDias = dias
        self.__fechaDevolucion = None

    #COMANDOS

    def establecerFechaDevolucion(self, fechaDev: "Fecha"):
        if not isinstance(fechaDev, Fecha):
            raise ValueError("Error")
        
        self.__fechaDevolucion = fechaDev

    #CONSULTAS

    def obtenerLibro(self)->Libro:
        return self.__libro
    def obtenerFechaPrestamo(self)->Fecha:
        return self.__fechaPrestamo
    def obtenerFechaDevolucion(self)->Fecha:
        return self.__fechaDevolucion
    
    def estaAtrasado(self, fecha: "Fecha")->bool:
        if not fecha.esAnterior(self.__fechaDevolucion):
            print(f"El libro deberia haberse devuelto el {self.__fechaDevolucion}")
            return True