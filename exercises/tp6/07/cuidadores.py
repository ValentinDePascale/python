from mascota import Mascota

class Cuidador:
    def __init__(self, nombre:str, direccion:str, telefono:int):
        if not isinstance(nombre, str) or nombre.strip() == ""  or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(direccion, str) or direccion.strip() == ""  or direccion.isspace():
            raise ValueError("La especie debe ser string valido")
        if not isinstance(telefono, int) or telefono < 0:
            raise ValueError("El telefono debe ser entera positiva")

        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mascotas = []


    def asignarMascota(self, mascota: "Mascota"):
        if not isinstance (mascota, Mascota):
            raise TypeError("La mascota debe ser instancia de mascota")
        self.__mascotas.append(mascota)


    def mostrarMascota(self)->"Mascota":

        print(f"Mascotas al cuidado de: {self.__nombre}")
        for i in self.__mascotas:
            print(i)


    def __str__(self):
        return(f"CUIDADOR"
               f"Nombre: {self.__nombre}\n"
               f"Direccion: {self.__direccion}\n"
               f"Telefono: {self.__telefono}\n"
               )

    