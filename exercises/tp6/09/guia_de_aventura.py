from visitante import Visitante
from atraccion import Atraccion

class Guia:
    def __init__(self, nombre:str, turno:str):
        if not isinstance(nombre, str) or nombre.isspace() or nombre.strip() == "":
            raise ValueError("El nombre debe ser un string")
        if not isinstance(turno, str) or turno.isspace() or turno.strip() == "":
            raise ValueError("El turno debe ser un string")

        self.__nombre = nombre
        self.__turno = turno


    def autorizarIngreso(self, visitante:"Vistante", atraccion:"Atraccion")->bool:
        if visitante.obtenerAltura() >= atraccion.obtenerEstaturaMinima():
            visitante.ingresoAtraccion(atraccion)
            return True
        else:
            return False
        

    def __str__(self):
        return (f"Nombre: {self.__nombre}, Turno: {self.__turno}")
