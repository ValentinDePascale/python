from empleado import Empleado

class test:
    @staticmethod
    def ejectuar():
        try:
            legajo = int(input("Ingrese legajo: "))
            cantHoras = int(input("Ingrese cantidad de horas: "))
            valorHora = float(input("Ingrese valor x hora: "))
            empleado2 = Empleado(legajo, cantHoras, valorHora)

            print(f"legajo: {empleado2.obtenerLegajo()}, sueldo: {empleado2.obtenerSueldo(cantHoras, valorHora)}")


        except ValueError as error:
            print(f"Error. {error}")
        except TypeError as error:
            print(f"Error. {error}")


if __name__ == "__main__":
    test.ejectuar()
