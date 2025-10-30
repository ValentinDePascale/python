from polizainmueble import PolizaInmueble

class Aseguradora:
    def __init__(self):

        self.__seguros = []


    def obtenerSeguros(self)->"PolizaInmueble":
        return self.__seguros

    def insertar(self, poliza:"PolizaInmueble"):
        if not isinstance(poliza, PolizaInmueble):
            raise TypeError("La poliza debe ser instancia de polizainmueble")
        
        if poliza not in self.__seguros:
            self.__seguros.append(poliza)
            print("Agregando poliza")
        else:
            print("La poliza ya existe en el seguro")

    def eliminar(self, poliza:"PolizaInmueble"):
        if not isinstance(poliza, PolizaInmueble):
            raise TypeError("La poliza debe ser instancia de polizainmueble")
        
        if poliza in self.__seguros:
            self.__seguros.remove(poliza)
            print("Eliminando poliza")

        else:
            print("La poliza no esta en el seguro, no se puede borrar")


    def existePoliza(self, poliza:"PolizaInmueble")->bool:
        if not isinstance(poliza, PolizaInmueble):
            raise TypeError("La poliza debe ser instancia de polizainmueble")
        if poliza in self.__seguros:
            return True
        else: 
            return False
        
    def hayPolizas(self)->bool:
        if self.__seguros:
            return True
        else: 
            return False
        
    def costoTotal(self)->float:
        total = 0
        for poli in self.__seguros:
            total += poli.costoPoliza()
        return total
    
    def esIgual(self, otraAseguradora:"Aseguradora")->bool:
        if not isinstance(otraAseguradora, Aseguradora):
            raise TypeError("La poliza debe ser instancia de polizainmueble")
        if self.obtenerSeguros == otraAseguradora.obtenerSeguros():
            return True
        else: 
            return False


