class Pais:
    def __init__(self, codigo:int, nombre:str, cantidadDispositivos:str):
        if not isinstance(codigo, int) or codigo < 0:
            raise ValueError("El codigo debe ser entero positivo")
        if not isinstance(nombre, str) or nombre.strip() == "" or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(cantidadDispositivos, str) or cantidadDispositivos.strip() == "" or cantidadDispositivos.isspace():
            raise ValueError("La cantidad de dispsitivos debe ser string valido")
        
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantidadDispotitivos = cantidadDispositivos

    
    def obtenerCantidadDispsitivos(self)->str:
        return self.__cantidadDispotitivos
    
    def obtenerNombre(self)->str:
        return self.__nombre

    def __str__(self):
        return (f"codigo: {self.__codigo}\n"
                f"nombre: {self.__nombre}\n"
                f"cantidad de dispositivos: {self.__cantidadDispotitivos}"
        )