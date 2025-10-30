class Inmueble:
    def __init__(self, codigo:int, domicilio:str, mCuadrados:int, estado:int):
         if not isinstance(codigo, int) or codigo < 0:
            raise ValueError("Error. El codigo debe ser entero positivo")
         if not isinstance(domicilio, str) or domicilio.strip() == "" or domicilio.isspace():
             raise ValueError("Error. El domicilio debe ser string valido")
         if not isinstance(mCuadrados, int) or mCuadrados < 0:
            raise ValueError("Error. Los metros cuadrados debe ser entero positivo")
         if not isinstance(estado, int) or estado < 0:
            raise ValueError("Error. El estado debe ser entero positivo")
         

         self._codigo = codigo
         self._domicilio = domicilio
         self._mCuadrados = mCuadrados
         self._estado = estado
    
    def obtenerCodigo(self)->int:
        return self._codigo

    def obtenerDomicilio(self)->str:
        return self._domicilio

    def obtenerMCuadrados(self)->int:
        return self._mCuadrados

    def obtenerEstado(self)->int:
        return self._estado
    
    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base < 0:
            raise ValueError("Error. El codigo debe ser entero positivo")
        return base + (100 * self.obtenerMCuadrados())
    
    def precioVenta(self, m2:float)->float:
        if not isinstance(m2, float) or m2 < 0:
            raise ValueError("Error. Los m2 debe ser reales positivo")
        
        return self.obtenerMCuadrados() * m2


    def __str__(self):
        return (f"Codigo:{self.obtenerCodigo()}, Domicilio:{self.obtenerDomicilio()}, Metros Cuadrados: {self.obtenerMCuadrados()}, Estado{self.obtenerEstado()}")