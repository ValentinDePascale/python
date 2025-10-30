from fecha import Fecha
class Socio:
    def __init__(self, nombre:str, fechaNacimiento:Fecha):
        if not isinstance(nombre, str) or nombre.isspace():
            raise ValueError("Error")
        if not isinstance(fechaNacimiento, Fecha):
            raise ValueError("Error")
        if not isinstance(fechaNacimiento, Fecha):
            raise ValueError("Error")
        
        self.__nombre = nombre
        self.__fechaNacimiento = fechaNacimiento
        self.__fechaPenalizacion = None
    
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre.isspace():
            raise ValueError("Error")
        self.__nombre = nombre

    def establecerFechaNacimiento(self, fecha:"Fecha"):
        if not isinstance(fecha, Fecha):
            raise ValueError("Error")
        self.__fechaNacimiento = fecha

    def establecerPenalizacion(self, fechaHasta: "Fecha"):
        if not isinstance(fechaHasta, Fecha):
            raise ValueError("Error")
        if self.__fechaPenalizacion != None:
            self.__fechaPenalizacion = fechaHasta


    #CONSULTAS

    def estaHabilitado(self, fecha:"Fecha")->bool:
        if not isinstance(fecha, Fecha):
            raise ValueError("Error")
        if self.__fechaPenalizacion == None or self.__fechaPenalizacion < fecha:
            return True
        return False
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerFechaNacimiento(self)->str:
        return self.__fechaNacimiento
    
    def obtenerFechaPenalizacion(self)->str:
        return self.__fechaPenalizacion

    def __str__(self):
        return (f"NOMBRE: {self.__nombre} \n"
        f" FECHA NACIMIENTO: {self.__fechaNacimiento} \n"
        f" FECHA PENALIZACION {self.__fechaPenalizacion}"
        )