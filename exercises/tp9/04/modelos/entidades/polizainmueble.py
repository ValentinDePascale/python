class PolizaInmueble:

    @classmethod
    def fromDiccionario(cls, diccionario:dict)-> "PolizaInmueble":
        if not isinstance(diccionario, dict):
            raise ValueError("El diccionario debe ser dict")
        
        if "numero" not in diccionario or "incendio" not in diccionario or "explosion" not in diccionario or "robo" not in diccionario:
            raise Exception("El diccionario debe contener las claves: 'numero', 'incendio', 'explosion' y 'robo' ")
        
        return cls(
            numero = diccionario["numero"],
            incendio = diccionario["incendio"],
            explosion = diccionario["explosion"],
            robo = diccionario["robo"]
        )


    def __init__(self, numero:int, incendio:float, explosion:float, robo:float):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("El número de póliza debe ser un entero positivo.")
        if not isinstance(incendio, (int, float)) or incendio <= 0:
            raise ValueError("La cobertura por incendio debe ser un número no negativo.")
        if not isinstance(explosion, (int, float)) or explosion <= 0:
            raise ValueError("La cobertura por explosión debe ser un número no negativo.")
        if not isinstance(robo, (int, float)) or robo <= 0:
            raise ValueError("La cobertura por robo debe ser un número no negativo.")


        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo


    def obtenerNumero(self)->int:
        return self._numero
    
    def obtenerIncendio(self)->float:
        return self._incendio
    
    def obtenerExplosion(self)->float:
        return self._explosion
    
    def obtenerRobo(self)->float:
        return self._robo
    

    def establecerNumero(self, numero:int):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("El número de póliza debe ser un entero positivo.")
        self._numero = numero

    
    def establecerIncendio(self, incendio:float):
        if not isinstance(incendio, (int, float)) or incendio <= 0:
            raise ValueError("La cobertura por incendio debe ser un número no negativo.")
        self._incendio = incendio  


    def establecerExplosion(self, explosion:float):
        if not isinstance(explosion, (int, float)) or explosion <= 0:
            raise ValueError("La cobertura por explosión debe ser un número no negativo.")
        self._explosion = explosion

    def establecerRobo(self, robo:float):
        if not isinstance(robo, (int, float)) or robo <= 0:
            raise ValueError("La cobertura por robo debe ser un numero no negativo")
        
        self._robo = robo


    def valorMensualPoliza(self)->float:
        calculoIncendio = self._incendio * 0.02 
        calculoExplosion = self._explosion * 0.01 
        calculoRobo = self._robo * 0.03 

        return (calculoIncendio + calculoExplosion + calculoRobo)


    def __str__(self):
        return f"Numero: {self._numero}, Incendio: {self._incendio}, Explosion: {self._explosion}, Robo {self._robo}"
    

    def toDiccionario(self):
        return{
            "numero": self._numero,
            "incendio": self._incendio,
            "explosion": self._explosion,
            "robo": self._robo
        }
    