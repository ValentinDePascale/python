from personal import Personal

class Mantenimiento(Personal):
    def __init__(self, nombre:str, apellido:str, dni:int, legajo:int, area:str):
        super().__init__(nombre, apellido, dni, legajo)

        self.__area = area

    def obtenerArea(self)->str:
        return self.__area

    def __str__(self):
        return (f"{super().__str__()}, Area: {self.obtenerArea()}")