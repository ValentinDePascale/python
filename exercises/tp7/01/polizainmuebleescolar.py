from polizainmueble import PolizaInmueble
class PolizaInmuebleEscolar(PolizaInmueble):
    def __init__(self, numero:int, incendio:float | int, explosion:float | int, robo:float | int, cantPersonas:int, montoEquipamiento:float | int, montoMobiliario:float | int, montoPersona:float | int):
        super().__init__(numero, incendio, explosion, robo)

        if not isinstance(cantPersonas, int) or cantPersonas < 0:
            raise ValueError("La cantidad de personas deben ser entero positivo")
        
        if not isinstance(montoEquipamiento, (float, int)) or montoEquipamiento < 0:
            raise ValueError("El monto equipamiento debe ser entero o real positivo")
        
        if not isinstance(montoMobiliario, (float, int)) or montoMobiliario < 0:
            raise ValueError("El monto equipamiento debe ser entero o real positivo")
        
        if not isinstance(montoPersona, (float, int)) or montoPersona < 0:
            raise ValueError("El monto equipamiento debe ser entero o real positivo")
        
        self.__cantPersonas = cantPersonas
        self.__montoEquipamiento = montoEquipamiento
        self.__montoMobiliario = montoMobiliario
        self.__montoPersona = montoPersona

    def obtenerCantPersonas(self) -> int:
        return self.__cantPersonas

    def obtenerMontoEquipamiento(self) -> float | int:
        return self.__montoEquipamiento
    
    def obtenerMontoMobiliario(self) -> float | int:
        return self.__montoMobiliario
    
    def obtenerMontoPersona(self) -> float | int:
        return self.__montoPersona

    def costoPoliza(self)->float:
        base = super().costoPoliza()
        extra = self.__montoEquipamiento + self.__montoMobiliario + (self.__montoPersona * self.__cantPersonas)

        return base + extra
    
    def __str__(self):
        return (f"{super().__str__()}, Cantidad personas: {self.obtenerCantPersonas()}, Monto equipamiento: {self.obtenerMontoEquipamiento()}, Monto mobiliario: {self.obtenerMontoMobiliario()}, Monto persona: {self.obtenerMontoPersona()}")