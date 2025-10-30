from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self,marca:str, modelo:str, patente:str, color:str, anio_fabricacion:int, precio:float, km:float, combustible:str, anchoManubrio: float, cilindrada: int):
        super().__init__(marca, modelo, patente, color, anio_fabricacion, precio, km, combustible)
        
        if not isinstance(anchoManubrio, float) or anchoManubrio <= 0:
            raise ValueError("El ancho del manubrio debe ser valido")
        
        if not isinstance(cilindrada, int) or cilindrada <= 0:
            raise ValueError("La cilindrada debe ser valido")
        self.__anchoManubrio = anchoManubrio
        self.__cilindrada = cilindrada

    def __str__(self):
        return (f"{super().__str__()}, Ancho de manubrio: {self.__anchoManubrio}, Cilindrada: {self.__cilindrada}")

    