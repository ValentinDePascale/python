from cuentabancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, saldo:float | int, cantExtracciones:int, cantDepositos:int, interesAnual:float, comisionMensual:float, limiteDescubierto:int, penalizaciones:int):
        super().__init__(saldo, cantExtracciones, cantDepositos, interesAnual, comisionMensual)

        if not isinstance(limiteDescubierto, (float, int)) or limiteDescubierto < 0:
                raise TypeError("El saldo debe ser entero o real valido")
        if not isinstance(penalizaciones, (float, int)) or penalizaciones < 0:
                raise TypeError("El saldo debe ser entero o real valido")
        
        self.__limiteDescubierto = limiteDescubierto
        self.__penalizaciones = penalizaciones


    def extraerDinero(self):
          return 