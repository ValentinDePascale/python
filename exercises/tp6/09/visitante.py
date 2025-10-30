from atraccion import Atraccion
class Visitante:
    def __init__(self, nombre:str, edad:int, altura:float, email:str):
        if not isinstance(nombre, str) or nombre.isspace() or nombre.strip() == "":
            raise ValueError("El nombre debe ser un string")
        
        if not isinstance(email, str) or email.isspace() or email.strip() == "":
            raise ValueError("El email debe ser un string")

        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__email = email
        self.__atraccion = []
        self.__tieneEntrada = False

    def ingresoAtraccion(self, atraccion:"Atraccion"):
            self.__atraccion.append(atraccion)

    def entradaAsignada(self):
        self.__tieneEntrada = True


    def visitanteTieneEntrada(self)->bool:
        return self.__tieneEntrada
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEdad(self)->int:
        return self.__edad
    
    def obtenerAltura(self)->float:
        return self.__altura
    
    def obtenerEmail(self)->str:
        return self.__email
    
    def __str__(self):
        return (f"Nombre: {self.__nombre}, Edad: {self.__edad}, Altura: {self.__altura}, Email: {self.__email}")
    
    