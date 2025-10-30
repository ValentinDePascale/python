from suscripcion import Suscripcion

class SuscripcionPaga(Suscripcion):
    def __init__(self, nombre:str, email:str, telefono:str, pais:Pais, tiempoSinPublicidad:int, tiempoReproducido:int):
        super().__init__(nombre, email, telefono, pais)