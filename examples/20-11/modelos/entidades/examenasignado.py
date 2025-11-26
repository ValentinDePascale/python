class ExamenAsignado:
    

    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        if not isinstance(diccionario, dict):
            raise ValueError("El diccionario debe ser instancia de dict")
        if "legajo" not in diccionario or "numeroTema" not in diccionario or "confirmado" not in diccionario:
            raise Exception("El diccionario debe contener las claves: 'legajo', 'numeroTema', 'confirmado'")

        return cls(
            legajo = diccionario["legajo"],
            numeroTema = diccionario["numeroTema"],
            confirmado = diccionario["confirmado"]
        )


    def __init__(self, legajo:int, numeroTema:int, confirmado:bool):
        if not isinstance(legajo, int) or legajo <= 0:
            raise TypeError("El legajo debe ser un entero positivo.")
        if not isinstance(numeroTema, int) or numeroTema <= 0:
            raise TypeError("El número de tema debe ser un entero positivo.")
        if not isinstance(confirmado, bool):
            raise TypeError("Confirmado debe ser un valor booleano.")
        
        self.__legajo = legajo
        self.__numeroTema = numeroTema
        self.__confirmado = confirmado

    def obtenerLegajo(self) -> int:
        return self.__legajo
    
    def obtenerNumeroTema(self) -> int:
        return self.__numeroTema
    
    def estaConfirmado(self) -> bool:   
        return self.__confirmado
    
    def establecerLegajo(self, legajo:int):
        if not isinstance(legajo, int) or legajo <= 0:
            raise TypeError("El legajo debe ser un entero positivo.")
        self.__legajo = legajo

    def establecerNumeroTema(self, numeroTema:int):
        if not isinstance(numeroTema, int) or numeroTema <= 0:
            raise TypeError("El número de tema debe ser un entero positivo.")
        self.__numeroTema = numeroTema

    def establecerConfirmado(self, confirmado:bool):
        if not isinstance(confirmado, bool):
            raise TypeError("Confirmado debe ser un valor booleano.")
        self.__confirmado = confirmado

    def __str__(self) -> str:
        if self.__confirmado:
            estado = "Confirmado"
        else:
            "No confirmado"
        return f"Examen Asignado - Legajo: {self.__legajo}, Tema: {self.__numeroTema}, Estado: {estado}"
    
    def toDiccionario(self) -> dict:
        return {
            "legajo": self.__legajo,
            "numeroTema": self.__numeroTema,
            "confirmado": self.__confirmado
        }
