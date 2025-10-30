class Propietario:
    def __init__(self, nombre:str, dni:str):
        if not isinstance(nombre, str) or nombre.strip() == "" or nombre.isspace():
            raise ValueError("Nombre tiene que ser un string")        
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("Dni tiene que ser un numero entero")
        self.__nombre = nombre
        self.__dni = dni


    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_dni(self) -> int:
        return self.__dni
    
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, DNI: {self.__dni}"