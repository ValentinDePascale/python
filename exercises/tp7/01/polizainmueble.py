class PolizaInmueble:
    def __init__(self, numero:int, incendio:float | int, explosion:float | int, robo:float | int):
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("Error. El numero debe ser entero positivo")
        if not isinstance(incendio, (float, int)) or incendio < 0:
            raise ValueError("Error. El incendio debe ser real positivo")
        if not isinstance(explosion, (float, int)) or explosion < 0:
            raise ValueError("Error. La explosion debe ser real positivo")
        if not isinstance(robo, (float, int)) or robo < 0:
            raise ValueError("Error. El robo debe ser real positivo")
       
        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo
    

    def obtenerNumero(self)->int:
        return self._numero

    def obtenerIncendio(self)->int:
        return self._incendio

    def obtenerExplosion(self)->int:
        return self._explosion

    def obtenerRobo(self)->int:
        return self._robo
    
    def costoPoliza(self)->float:
        return (self._incendio + self._explosion + self._robo)
    
    def __str__(self):
        return (f"Numero: {self.obtenerNumero()}, Incendio: {self.obtenerIncendio()}, Explosion: {self.obtenerExplosion()}, Robo: {self.obtenerRobo()}")
        