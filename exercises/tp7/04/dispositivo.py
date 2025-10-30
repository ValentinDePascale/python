class Dispositivo:
    def __init__(self, id:int, nombre:str, tipo:str):
        if not isinstance(id, int) or id < 0:
            raise ValueError("El id debe ser entero positivo")
        if not isinstance(nombre, str) or nombre.strip() == "" or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(tipo, str) or tipo.strip() == "" or tipo.isspace():
            raise ValueError("El nombre debe ser string valido")
        
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo



    def obtenerNombre(self)->str:
        return self.__nombre
    
    def __str__(self):
        return (f"id: {self.__id}\n"
                f"nombre: {self.__nombre}\n"
                f"tipo: {self.__tipo}"
        )
