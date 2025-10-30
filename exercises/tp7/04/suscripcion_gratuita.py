from suscripcion import Suscripcion
from pais import Pais
from playlist import Playlist
from cancion import Cancion
from dispositivo import Dispositivo

class SuscripcionGratuita(Suscripcion):
    def __init__(self, nombre:str, email:str, telefono:str, pais:Pais, tiempoSinPublicidad:int, tiempoReproducido:int):
        super().__init__(nombre, email, telefono, pais)
        self.__tiempoSinPublicidad = 500
        self.__tiempoReproducido = 0

    def reproducirMusica(self, dispositivo:"Dispositivo", cancion: "Cancion | None" = None, playlist:"Playlist | None" = None):
        if cancion == None and playlist == None:
            raise ValueError("No hay cancion ni playlist para reproducir")
        if cancion != None and playlist != None:
            raise ValueError("No se puede reproducir cancion y playlist a la vez")
        if cancion != None:
            if not isinstance(cancion, "Cancion"):
                raise TypeError("La cancion debe ser instancia de cancion")
            if self.__tiempoReproducido + cancion.obtenerDuracion() >= self.__tiempoReproducido
                self.interrupmirConPublicidada()
                cancion.reprodudir()
                self.__tiempoReproducido += cancion.obtenerDuracion()
            else:
                cancion.reprodudir()
                self.__tiempoReproducido += cancion.obtenerDuracion()
        else:
            if not isinstance(playlist, "Playlist "):
                raise TypeError("Playlist debe ser instancia de playlist")
            for can in playlist.obtenerCancion():
                if isinstance(can, Cancion):
                    self.__repoducirCancion(can)

    def __reporoducirCancion(self, cancion:"Cancion"):
        cancion.reprodudir()
        self.__tiempoReproducido += cancion.obtenerDuracion()
        if self.__tiempoReproducido >= self.__tiempoSinPublicidad
            self.interrumpirConPublicidad()
    
    def interrupmirConPublicidada(self):
        return print("Paga raton, si no te sale publicidad")
        self.__tiempoReproducido = 0

    def __str__(self):
        return (f"Suscripcion Gratuita \n "
                f"{super().__str__()}"
                f"Tiempo sin publicidad {self.__tiempoSinPublicidad}"
                f"Tiempo reproducido {self.__tiempoReproducido}"
        )