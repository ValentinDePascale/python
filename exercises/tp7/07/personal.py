from abc import ABC, abstractmethod
class Personal(ABC):
    def __init__(self, dni:int, nombre:str, apellido:str, fecha_ingreso:str):

        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_ingreso = fecha_ingreso


    def obtenerDni(self)->int:
        return self._dni


    @abstractmethod
    def salarioFinal(self)->float:
        pass

    def __str__(self):
        return (
            f"DNI: {self._dni}\n"
            f"Nombre: {self._nombre}\n"
            f"Apellido: {self._apellido}\n"
            f"Fecha Ingreso: {self._fecha_ingreso}\n"
        )
    
    