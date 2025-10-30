from personal import Personal

class SalarioFijo(Personal):
    def __init__(self, dni:int, nombre:str, apellido:str, fecha_ingreso:str, sueldoBasico:float, antiguedad:int):
        super().__init__(dni, nombre, apellido, fecha_ingreso)

        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad



    def salarioFinal(self)->float:
        sueldo = 0
        if self.__antiguedad >= 2 and self.__antiguedad <= 5:
            sueldo = self.__sueldoBasico * 1.05
        elif self.__antiguedad > 5:
            sueldo = self.__sueldoBasico * 1.10
        else:
            sueldo = self.__sueldoBasico

        return sueldo


         