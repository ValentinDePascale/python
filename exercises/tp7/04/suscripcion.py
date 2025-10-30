from abc import ABC, abstractmethod
from pais import Pais
from playlist import Playlist

class Suscripcion(ABC):
    def __init__(self, nombre:str, email:str, telefono:str, pais:Pais):
        if not isinstance(nombre, str) or nombre.strip() == "" or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(email, str) or email.strip() == "" or email.isspace():
            raise ValueError("El email debe ser string valido")
        if not "@" in email:
            raise ValueError("El email debe tener @")
        if not isinstance(telefono, str) or telefono.strip() == "" or telefono.isspace():
            raise ValueError("El telefono debe ser string valido")

        if not isinstance (pais, Pais):
            raise TypeError("Pais debe ser instancia de pais") 

        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._pais = pais


    @abstractmethod
    def reproducirMusica(self, dispositivo:"Dispositivo", cancion: "Cancion | None" = None, playlist: "Playlist | None" = None):
        pass 

    

    def __str__(self):
        return (f"nombre: {self._nombre}\n"
                f"email: {self._email}\n"
                f"telefono: {self._telefono}\n"
                f"pais: {self._pais.obtenerNombre()}"
        )