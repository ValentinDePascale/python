from empleado import Empleado

class tester:
    @staticmethod
    def ejecutar():
        try:
            legajo = int(input("Ingrese legajo: "))
            horas =  int(input("Ingrese horas de trabajao: "))
            valor = float(input("Ingrese valor x hora: "))
            empleado = Empleado(legajo)

            empleado.establecerHorasTrabajadas(horas)
            empleado.establecerValorHora(valor)


            print(f"Datos empleado")
            print(f"Legajo: {empleado.obtenerLegajo()}")
            print(f"Sueldo: {empleado.obtenerSueldo(horas, valor)}")

            
        except TypeError as error:
            print(f"Error {error}")
        except ValueError as error:
            print(f"Error {error}" )

if __name__ == "__main__":
    tester.ejecutar()


