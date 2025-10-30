from inmueble import Inmueble
import math

class Quinta(Inmueble):
    def __init__(self, codigo:int, domicilio:str, mCuadrados:int, estado:int, metrosParque:int):
        super().__init__(codigo, domicilio, mCuadrados, estado)
        if not isinstance(metrosParque, int) or metrosParque < 0:
            raise ValueError("Error. Los metros de paque comunes deben ser reales positivos")
        
        self.__metrosParque = metrosParque


    def obtenerMetrosParque(self):
        return self.__metrosParque

    def costoAlquiler(self, base)->float:
        if not isinstance(base, int) or base < 0:
            raise ValueError("Error. La base comunes deben ser reales positivos")
        

        cantMetrosParque = float(self.__metrosParque) / 15 
        math.floor(cantMetrosParque)

        if cantMetrosParque > 0:
            return base + (100 * self.obtenerMCuadrados()) + (cantMetrosParque * 500) 
        else:
            return super().costoAlquiler(base)
        
    def precioVenta(self, m2):
        return super().precioVenta(m2)
    
    def __str__(self):
        return (f"{super().__str__()}, Metros de Parque: {self.obtenerMetrosParque()}")
    
class Test:
    @staticmethod
    def run():
        d1 = Quinta(1, "Alvear 208", 200, 10, 300)
        
        print(d1.costoAlquiler(1000))
        print(d1.precioVenta(150.13))

        print(d1)

if __name__ == "__main__":
    Test.run()