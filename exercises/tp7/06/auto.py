from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self,marca:str, modelo:str, patente:str, color:str, anio_fabricacion:int, precio:float, km:float, combustible:str, cantPuertas:int, tieneAire:bool):
        super().__init__(marca, modelo, patente, color, anio_fabricacion, precio, km, combustible)
        
        if not isinstance(cantPuertas, int) or cantPuertas <= 0:
            raise ValueError("La cantPuertas debe ser valido")
        
        if not isinstance(tieneAire, bool):
            raise TypeError("Indicar si tiene aire con true o false")
        self.__cantPuertas = cantPuertas
        self.__tieneAire = tieneAire

    def __str__(self):
        return (f"{super().__str__()}, Cantidad de puertas: {self.__cantPuertas}, Tiene aire: {self.__tieneAire}")

    