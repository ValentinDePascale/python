from personal import Personal

class Administrativo(Personal):
    def __init__(self, nombre:str, apellido:str, dni:int, legajo:int, posicion:str):
        super().__init__(nombre, apellido, dni, legajo)

        self.__posicion = posicion

    def obtenerPosicion(self)->str:
        return self.__posicion

    def __str__(self):
        return (f"{super().__str__()}, Posicion: {self.obtenerPosicion()}")