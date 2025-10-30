from abc import ABC, abstractmethod


class Personal(ABC):
    def __init__(self, nombre:str, apellido:str, dni:int, legajo:int):
        
        
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._legajo = legajo


    def obtenerNombre(self)->str:
        return self._nombre

    def obtenerApellido(self)->str:
        return self._apellido

    def obtenerDNI(self)->int:
        return self._dni

    def obtenerLegajo(self)->int:
        return self._legajo

    def __str__(self):
        return (f"Nombre: {self.obtenerNombre()}, Apellido: {self.obtenerApellido()}, DNI: {self.obtenerApellido()}, Legajo: {self.obtenerLegajo()}")