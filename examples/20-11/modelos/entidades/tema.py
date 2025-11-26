class Tema:

    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        if not isinstance(diccionario, dict):
            raise ValueError("El diccionario debe ser instancia de dict")
        if "numero" not in diccionario or "nombre" not in diccionario or "enunciado" not in diccionario:
            raise Exception("El diccionario debe contener las claves: 'numero', 'nombre', 'enunciado'")

        return cls(
            numero = diccionario["numero"],
            nombre = diccionario["nombre"],
            enunciado = diccionario["enunciado"]
        )



    def __init__(self, numero:int, nombre:str, enunciado:str):
        if not isinstance(numero, int) or numero <= 0:
            raise TypeError("El número debe ser un entero positivo.")
        if not isinstance(nombre, str) or not nombre.strip() == "" or nombre.isspace():
            raise TypeError("El nombre debe ser una cadena no vacía.")
        if not isinstance(enunciado, str) or not enunciado.strip() == "" or enunciado.isspace():
            raise TypeError("El enunciado debe ser una cadena no vacía.")
        
        self.__numero = numero
        self.__nombre = nombre
        self.__enunciado = enunciado
        

    def obtenerNumero(self) -> int:
        return self.__numero

    def obtenerNombre(self) -> str:
        return self.__nombre

    def obtenerEnunciado(self) -> str:
        return self.__enunciado
    

    def establecerNumero(self, numero:int):
        if not isinstance(numero, int) or numero <= 0:
            raise TypeError("El número debe ser un entero positivo.")
        self.__numero = numero

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or not nombre.strip() == "" or nombre.isspace():
            raise TypeError("El nombre debe ser una cadena no vacía.")
        self.__nombre = nombre

    def establecerEnunciado(self, enunciado:str):
        if not isinstance(enunciado, str) or not enunciado.strip() == "" or enunciado.isspace():
            raise TypeError("El enunciado debe ser una cadena no vacía.")
        self.__enunciado = enunciado

    def __str__(self) -> str:
        return f"Tema {self.__numero}: {self.__nombre}\nEnunciado: {self.__enunciado}"
    
    def toDiccionario(self)-> dict:
        return {
            "numero": self.__numero,
            "nombre": self.__nombre,
            "enunciado": self.__enunciado
        }