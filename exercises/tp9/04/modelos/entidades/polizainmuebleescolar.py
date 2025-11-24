from modelos.entidades.polizainmueble import PolizaInmueble


class PolizaInmuebleEscolar(PolizaInmueble):

    @classmethod
    def fromDiccionario(cls, diccionario:dict) -> "PolizaInmuebleEscolar":
        if not isinstance(diccionario, dict):
            raise ValueError("EL diccionario tiene que ser dict")
        
                
        if ("numero" not in diccionario or "incendio" not in diccionario or "explosion" not in diccionario or "robo" not in diccionario or
        "cant_personas" not in diccionario or "monto_equipamiento" not in diccionario or "monto_mobiliario" not in diccionario or "monto_persona" not in diccionario):
            raise Exception("Se esperaban las claves: 'numero', 'incendio', 'explosion', 'robo', 'cant_personas', 'monto_equipamiento', 'monto_mobiliario', 'monto_persona'")
        
        return cls(
            numero = diccionario["numero"],
            incendio = diccionario["incendio"],
            explosion = diccionario["explosion"],
            robo = diccionario["robo"],
            cant_personas = diccionario["cant_personas"],
            monto_equipamiento = diccionario["monto_equipamiento"],
            monto_mobiliario = diccionario["monto_mobiliario"],
            monto_persona = diccionario["monto_persona"]
        )


    def __init__(self, numero:int, incendio:float | int, explosion:float | int, robo:float | int, cant_personas : int, monto_equipamiento:float | int, monto_mobiliario:float | int, monto_persona:float | int):
        super().__init__(numero, incendio, explosion, robo)

        if not isinstance(cant_personas, int) or cant_personas < 0:
            raise ValueError("La cantidad de personas debe ser un entero no negativo.")
        
        if not isinstance(monto_equipamiento, (int, float)) or monto_equipamiento < 0:
            raise ValueError("El monto de equipamiento debe ser un número no negativo.")
        
        if not isinstance(monto_mobiliario, (int, float)) or monto_mobiliario < 0:
            raise ValueError("El monto de mobiliario debe ser un número no negativo.")
        
        if not isinstance(monto_persona, (int, float)) or monto_persona < 0:
            raise ValueError("El monto por persona debe ser un número no negativo.")

        self.__cant_personas = cant_personas
        self.__monto_equipamiento = monto_equipamiento
        self.__monto_mobiliario = monto_mobiliario
        self.__monto_persona = monto_persona


    def obtenerCantPersonas(self) -> int:
        return self.__cant_personas
    
    def obtenerMontoEquipamiento(self) -> float | int:
        return self.__monto_equipamiento
    
    def obtenerMontoMobiliario(self) -> float | int:
        return self.__monto_mobiliario
    
    def obtenerMontoPersona(self) -> float | int:
        return self.__monto_persona


    def establecerCantPersonas(self, cantPersona:int):
        if not isinstance(cantPersona, int) or cantPersona < 0:
            raise ValueError("La cantidad de personas debe ser un entero no negativo.")
        self.__cant_personas = cantPersona  

    def establecerMontoEquipamiento(self, monto_equipamiento:float | int):
        if not isinstance(monto_equipamiento, (int, float)) or monto_equipamiento < 0:
            raise ValueError("El monto de equipamiento debe ser un número no negativo.")
        self.__monto_equipamiento = monto_equipamiento


    def establecerMontoMobiliario(self, monto_mobiliario:float | int):
        if not isinstance(monto_mobiliario, (int, float)) or monto_mobiliario < 0:
            raise ValueError("El monto de mobiliario debe ser un número no negativo.")
        self.__monto_mobiliario = monto_mobiliario

    def establecerMontoPersona(self, monto_persona:float | int):
        if not isinstance(monto_persona, (int, float)) or monto_persona < 0:
            raise ValueError("El monto por persona debe ser un número no negativo.")
        self.__monto_persona = monto_persona


    def valorMensualPoliza(self)->float:
        calculoIncendio = self._incendio * 0.01
        calculoExplosion = self._explosion * 0.01
        calculoRobo = self._robo * 0.02
        calculoEquipamiento = self.__monto_equipamiento * 0.01
        calculoMobiliaro = self.__monto_mobiliario * 0.01
        calculoPersona = (self.__monto_persona * self.__cant_personas) * 0.01

        return (calculoIncendio+calculoExplosion+calculoRobo+calculoEquipamiento+calculoMobiliaro+calculoPersona)
    

    def __str__(self):
        return (f"{super().__str__()}, Cantidad de personas: {self.__cant_personas}, Monto equipamiento: {self.__monto_equipamiento}, Monto mobiliario: {self.__monto_mobiliario}, Monto persona: {self.__monto_persona}")
    

    def toDiccionario(self):
        return {
            "numero": self._numero,
            "incendio": self._incendio,
            "explosion": self._explosion,
            "robo": self._robo,
            "cant_personas": self.__cant_personas,
            "monto_equipamiento": self.__monto_equipamiento,
            "monto_mobiliario": self.__monto_mobiliario,
            "monto_persona": self.__monto_persona
        }