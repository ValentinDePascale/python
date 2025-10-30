class Atraccion:
    def __init__(self, nombre:str, tipo:str, emocion:str, estatura_min:float):
        if not isinstance(nombre, str) or nombre.isspace() or nombre.strip() == "":
            raise ValueError("El nombre debe ser un string")
        
        if not isinstance(tipo, str) or tipo.isspace() or tipo.strip() == "":
            raise ValueError("El tipo debe ser un string")
        
        if not isinstance(emocion, str) or emocion.isspace() or emocion.strip() == "":
            raise ValueError("La emocion debe ser un string")

        self.__nombre = nombre
        self.__tipo = tipo
        self.__emocion = emocion
        self.__estatura_min = estatura_min
        self.__turno = []


    def establecerTurno(self, turno):
        if turno in ("Mañana", "Tarde", "Noche"):
            self.__turno.append(turno)

    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerTipo(self)->str:
        return self.__tipo
    
    def obtenerEmocion(self)->str:
        return self.__emocion
    
    def obtenerEstaturaMinima(self)->float:
        return self.__estatura_min
    


    def __str__(self):
        return (f"Nombre: {self.__nombre}, Tipo: {self.__tipo}, Emocion: {self.__emocion}, Estatura Minima: {self.__estatura_min}")