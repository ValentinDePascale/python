from fecha import Fecha
import random
class test:
    @staticmethod
    def ejecutar():
        #constructores
        fecha1 = Fecha(9, 4, 2005)
        fecha2 = Fecha(27, 8, 2005)

        print("-"*40+" FECHAS "+"-"*40)

        mostrarfecha1 = f"{fecha1.obtenerDia()}/{fecha1.obtenerMes()}/{fecha1.obtenerAnio()}"
        mostrarfecha2 = f"{fecha2.obtenerDia()}/{fecha2.obtenerMes()}/{fecha2.obtenerAnio()}"
        print(f"DIA: {fecha1.obtenerDia()}")
        print(f"MES: {fecha1.obtenerMes()}")
        print(f"AÑO: {fecha1.obtenerAnio()}")
        print() 

        print(f"DIA: {fecha2.obtenerDia()}")
        print(f"MES: {fecha2.obtenerMes()}")
        print(f"AÑO: {fecha2.obtenerAnio()}")

        if fecha1.esAnterior(fecha2):
            print(f"{mostrarfecha1} es anterior a la {mostrarfecha2}")
        else:
            print(f"{mostrarfecha2} es anterior a {mostrarfecha1}")


        print()

        sumarDias = random.randint(1, 100)
        print (f"{mostrarfecha1} + {sumarDias} dias") 
        fechaNueva = fecha1.sumaDias(sumarDias)
        print(f"{fechaNueva.obtenerDia()}/{fechaNueva.obtenerMes()}/{fechaNueva.obtenerAnio()}")

        print()
        print(f"Dia siguiente de {mostrarfecha2}")
        diaSiguiente = fecha2.diaSiguiente()
        print(f"{diaSiguiente.obtenerDia()}/{diaSiguiente.obtenerMes()}/{diaSiguiente.obtenerAnio()}")

        print()

        if fecha1.esIgualQue(fecha2):
            print(f"Fecha 1 y 2 son iguales: {mostrarfecha1} y {mostrarfecha2}")
        else:
            print(f"{mostrarfecha1} no es igual a {mostrarfecha2}")




if __name__ == "__main__":
    test.ejecutar()