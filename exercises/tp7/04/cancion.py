class Cancion:
    def __init__(self, codigo:int, nombre:str, duracion:int, genero:str):
        if not isinstance(codigo, int) or codigo < 0:
            raise ValueError("El codigo debe ser entero positivo")
        if not isinstance(nombre, str) or nombre.strip() == "" or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(duracion, int) or duracion < 0:
            raise ValueError("La cancion debe tener duracion entera positivo")
        if not isinstance(genero, str) or genero.strip() == "" or genero.isspace():
            raise ValueError("El genero debe ser string")
        
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__genero = genero

    
    def reprodudir(self)->str:
        return print(f"reproduciendo cancion: {self.obtenerNombre()} {self.obtenerDuracion()}")
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerDuracion(self)->int:
        return self.__duracion
    
    def __str__(self):
        return (f"codigo: {self.__codigo}\n"
                f"nombre: {self.__nombre}\n"
                f"duracion: {self.__duracion}\n"
                f"genero: {self.__genero}"
        )