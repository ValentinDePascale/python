from personal import Personal
from salariofijo import SalarioFijo
from comision import Comision


class Empresa:
    def __init__(self, nombre:str):

        self.__nombre = nombre
        self.__empleados = []

    def agregarEmpleado(self, empleado:"Personal"):
        if not isinstance(empleado, Personal):
            raise TypeError("El empleado debe ser instancia de Personal")
        
        if empleado not in self.__empleados:
            self.__empleados.append(empleado)
        else:
            print("El empleado ya esta ingresado")
        

    def eliminarEmpleado(self, empleado:"Personal"):
        if not isinstance(empleado, Personal):
            raise TypeError("El empleado debe ser instancia de Personal")
        
        if empleado in self.__empleados:
            self.__empleados.remove(empleado)
        else:
            print("El empleado no esta ingresado")

    def consultarSalarioDni(self, dni:int)->Personal:

        for emple in self.__empleados:
            if emple.obtenerDni() == dni:
                return emple.salarioFinal()
 

    def masClientes(self)->Personal:
        masEmpleados = -1
        empleado = None
        for emple in self.__empleados:
            if isinstance(emple, Comision):
                if emple.obtenerNumClientes() > masEmpleados:
                    masEmpleados = emple.obtenerNumClientes()
                    empleado = emple

        return empleado
