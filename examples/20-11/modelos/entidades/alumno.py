class Alumno:
    __ID : 0

    @classmethod
    def fromDiccionario(cls, diccionario:dict)->"Alumno":
        if not isinstance(diccionario, dict):
            raise ValueError("El diccionario debe ser instancia de dict")
        if "id" not in diccionario or "legajo" not in diccionario or "nombre" not in diccionario or "apellido" not in diccionario:
            raise Exception("El diccionario debe contener las claves: 'id', 'legajo', 'nombre', 'apellido'")

        return cls(
            id = diccionario["id"],
            legajo = diccionario["legajo"],
            nombre = diccionario["nombre"],
            apellido = diccionario["apellido"]
        )

    @classmethod
    def estableceUltimoId(cls, id:int):
        if not isinstance(id, int) or id < 0:
            raise TypeError("El ID debe ser un entero no negativo.")
        cls.__ID = id

    @classmethod
    def obtenerUltimoId(cls) -> int:
        return cls.__ID
    
    @classmethod
    def generarID(cls)->int:
        cls.__ID += 1
        return cls.__ID


    def __init__(self, legajo:int, nombre:str, apellido:str):
        if not isinstance(legajo, int) or legajo <= 0:
            raise TypeError("El legajo debe ser un entero positivo.")
        if not isinstance(nombre, str) or not nombre.strip() == "" or nombre.isspace(): 
            raise TypeError("El nombre debe ser una cadena no vacía.")
        if not isinstance(apellido, str) or not apellido.strip() == "" or apellido.isspace():
            raise TypeError("El apellido debe ser una cadena no vacía.")
                
        self.__legajo = legajo
        self.__nombre = nombre
        self.__apellido = apellido


    def obtenerLegajo(self) -> int:
        return self.__legajo
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerApellido(self) -> str:
        return self.__apellido
    
    def establecerLegajo(self, legajo:int):
        if not isinstance(legajo, int) or legajo <= 0:
            raise TypeError("El legajo debe ser un entero positivo.")
        self.__legajo = legajo

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or not nombre.strip() == "" or nombre.isspace(): 
            raise TypeError("El nombre debe ser una cadena no vacía.")
        self.__nombre = nombre

    def establecerApellido(self, apellido:str):
        if not isinstance(apellido, str) or not apellido.strip() == "" or apellido.isspace():
            raise TypeError("El apellido debe ser una cadena no vacía.")
        self.__apellido = apellido

    def __str__(self) -> str:
        return f"ID: {self.__ID}, Legajo: {self.__legajo}, Nombre: {self.__nombre}, Apellido: {self.__apellido}"

    def toDiccionario(self)->dict:
        return {
            "id": self.__ID,
            "legajo": self.__legajo,
            "nombre": self.__nombre,
            "apellido": self.__apellido
        }        