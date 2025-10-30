from personal import Personal

class Comision(Personal):
    def __init__(self, dni:int, nombre:str, apellido:str, fecha_ingreso:str, salarioMinimo:float, numClientes:int, montoCliente:float):
        super().__init__(dni, nombre, apellido, fecha_ingreso)

        self.__salarioMinimo = salarioMinimo
        self.__numClientes = numClientes
        self.__montoCliente = montoCliente

    def obtenerNumClientes(self):
        return self.__numClientes

    def salarioFinal(self)->float:
        sueldo = 0
        if (self.__numClientes * self.__montoCliente) >= self.__salarioMinimo:
            sueldo = (self.__numClientes * self.__montoCliente)
        else:
            sueldo = self.__salarioMinimo
        

        return sueldo
