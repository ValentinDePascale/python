from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, saldo:float | int, cantExtracciones:int, cantDepositos:int, interesAnual:float, comisionMensual:float):

        if not isinstance(saldo, (float, int)) or saldo < 0:
            raise TypeError("El saldo debe ser entero o real valido")
        if not isinstance(cantExtracciones, (float, int)) or cantExtracciones < 0:
                    raise TypeError("La cantExtracciones debe ser entero o real valido")
        if not isinstance(cantDepositos, (float, int)) or cantDepositos < 0:
                    raise TypeError("La cant Depositos saldo debe ser entero o real valido")
        if not isinstance(interesAnual, (float, int)) or interesAnual < 0:
                    raise TypeError("El interesAnual debe ser entero o real valido")
        if not isinstance(comisionMensual, (float, int)) or comisionMensual < 0:
                    raise TypeError("La comision mensual debe ser entero o real valido")
        

        self._saldo = saldo
        self._cantExtracciones = cantExtracciones
        self._cantDepositos = cantDepositos
        self._interesAnual = interesAnual
        self._comisionMensual = comisionMensual

    @abstractmethod
    def extraerDinero(self):
        pass

    @abstractmethod
    def depositarDinero(self):
        pass

    @abstractmethod
    def extractoMensual(self):
        pass


    def __str__(self):
        return (f"Saldo \n"
                f"CuentaBancaria\n"
                f"Saldo: ${self._saldo:,.2f}\n"
                f"Cantidad extracciones: {self._cantExtracciones}\n"
                f"Cantidad depósitos: {self._cantDepositos}\n"
                f"Interés anual: {self._interesAnual:.2f}%\n"
                f"Comisión mensual: ${self._comisionMensual:,.2f}"
        )