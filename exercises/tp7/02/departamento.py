from inmueble import Inmueble
class Departamento(Inmueble):
    def __init__(self, codigo:int, domicilio:str, mCuadrados:int, estado:int, gastosComunes:float, cochera:bool):
        super().__init__(codigo, domicilio, mCuadrados, estado)
        if not isinstance(gastosComunes, float) or gastosComunes < 0:
            raise ValueError("Error. Los gastos comunes deben ser reales positivos")
        
        if not isinstance(cochera, bool):
            raise TypeError("Error. La cochera debe ser boolean")
        
        self.__gastosComunes = gastosComunes
        self.__cochera = cochera


    def obtenerGastosComunes(self)->float:
        return self.__gastosComunes
    
    def obtenerCochera(self)->bool:
        return self.__cochera

    def costoAlquiler(self, base)->float:
        if not isinstance(base, int) or base < 0:
            raise ValueError("Error. La base comunes deben ser reales positivos")

        if self.obtenerCochera:
            return base + (100 * self.obtenerMCuadrados()) + 2000 
        else:
            return super().costoAlquiler(base)
        
    def precioVenta(self, m2):
        return super().precioVenta(m2)
    
    def __str__(self):
        return (f"{super().__str__()}, Gatos comunes: {self.obtenerGastosComunes()}, Cochera: {self.obtenerCochera()}")
    

