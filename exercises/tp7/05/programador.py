from personal import Personal

class Programador(Personal):
    def __init__(self, nombre:str, apellido:str, dni:int, legajo:int, proyecto:str):
        super().__init__(nombre, apellido, dni, legajo)

        self.__proyecto = proyecto

    def obtenerProyecto(self)->str:
        return self.__proyecto

    def __str__(self):
        return (f"{super().__str__()}, Proyecto: {self.obtenerProyecto()}")