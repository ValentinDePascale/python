from participante import Participante

class Evento:
    def __init__(self, nombre:str, fecha:str, descripcion:str):
        if not isinstance(nombre, str) or nombre.strip() == ""  or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(fecha, str) or fecha.strip() == ""  or fecha.isspace():
            raise ValueError("La fecha debe ser string valido")
        if not isinstance(descripcion, str) or descripcion.strip() == ""  or descripcion.isspace():
            raise ValueError("La descripcion debe ser string valido ")


        self.__nombre = nombre
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__participantes = []

    def establecerParticipantes(self, participante:"Participantes"):
        if not isinstance(participante, Participante):
            raise TypeError("Error")
        
        if participante not in self.__participantes:
            self.__participantes.append(participante)
        else:
            print("El participante ya esta en el evento")


    def __str__(self):
        return (f"Nombre: {self.__nombre}, Fecha: {self.__fecha}, Descripcion: {self.__descripcion}")