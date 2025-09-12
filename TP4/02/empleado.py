class Empleado:
    #atributos de instancia
    def __init__(self, legajo:int, horasTrabajadasMes:int = 0, valorHora:float = 0.0):
        if not isinstance(legajo, int):
            raise TypeError("Error. El legajo debe ser entero.")
        if legajo < 0:
            raise ValueError("Error. El legajo debe ser positivo")
        if not isinstance(horasTrabajadasMes, int):
            raise TypeError("Error. La cantidad de horas trabajadas debe ser entero")
        if horasTrabajadasMes < 0:
            raise ValueError("Error. La cantidad de horas deben ser positivas")
        if not isinstance(valorHora, float):
            raise TypeError("Error. El valor de la hora debe ser decimal")
        if valorHora < 0:
            raise ValueError("Error. El valor de la hora debe ser positivo")
        self.__legajo = legajo
        self.__horasTrabajadasMes = horasTrabajadasMes
        self.__valorHora = valorHora

#Comandos

    def establecerHorasTrabajadas(self, cantHoras:int):
        self.__horasTrabajadasMes = cantHoras

    def establecerValorHora(self, valorHora:float):
        self.__valorHora  = valorHora

    def obtenerLegajo(self)->int:
        return self.__legajo
    
    def obtenerHorasTrabajas(self)->int:
        return self.__horasTrabajadasMes
    
    def obtenerValorHora(self)->int:
        return self.__valorHora
    
    def obtenerSueldo(self, horasTrabajadasMes:int, valorHora:float)->float:
        return horasTrabajadasMes * valorHora


   





