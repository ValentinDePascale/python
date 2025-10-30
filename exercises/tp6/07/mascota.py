class Mascota:
    def __init__(self, nombre:str, especie:str, edad:int, descripcion:str):
        if not isinstance(nombre, str) or nombre.strip() == ""  or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(especie, str) or especie.strip() == ""  or especie.isspace():
            raise ValueError("La especie debe ser string valido")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edada debe ser entera positiva")
        if not isinstance(descripcion, str) or descripcion.strip() == ""  or descripcion.isspace():
            raise ValueError("La descripcion debe ser string valido")
        
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__descripcion = descripcion
        self.__cuidador = None
    
    def __str__(self):
        return(f"Nombre: {self.__nombre} \n"
               f"Especie {self.__especie} \n"
               f"Edad: {self.__edad} \n"
               f"Descripcion: {self.__descripcion}")
        