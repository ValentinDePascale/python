from automovil import Automovil
import random

class test:
    @staticmethod
    def ejecutar():
        try:
            automovil = Automovil("BMW", "X5", 2022, 250.0, 70.0)
            cantIteraciones = int(input("Ingrese cantidad de iteraciones "))
            numRandom = random.randint(10, 100)

            for i in range (cantIteraciones):
                numRandom = random.randint(0,3)
                valoresRandom = random.randint(10, 100)

                if numRandom == 0:
                    print(f"Velocidad:{automovil.obtenerVelocidadActual()}")
                    automovil.acelerar(valoresRandom)
                    print(f"Acelerando {valoresRandom}")
                    print(f"Velocidad actual: {automovil.obtenerVelocidadActual()}")
                elif numRandom == 1:
                    print(f"Velocidad: {automovil.obtenerVelocidadActual()}")
                    automovil.desacelerar(valoresRandom)
                    print(f"Desacelerando {valoresRandom}")
                    print(f"Velocidad actual: {automovil.obtenerVelocidadActual()}")
                elif numRandom == 2:
                    print(f"Velocidad:{automovil.obtenerVelocidadActual()}")
                    automovil.frenarPorCompleto()
                    print("Frenando")
                    print(f"Velocidad actual: {automovil.obtenerVelocidadActual()}") 
                elif numRandom == 3:
                    print(f"Velocidad:{automovil.obtenerVelocidadActual()}")
                    print(f"El tiempo de llegada a los 15km es {automovil.calcularMinutosParaLlegar(valoresRandom)}minutos")
                else:
                   raise ValueError("Mala generacion de numero random")  
        except ValueError as error:
            print(f"Error. {error}")
        except TypeError as error:
            print(f"Error. {error}")
        


if __name__ == "__main__":
    test.ejecutar()
 