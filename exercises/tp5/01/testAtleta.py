from atleta import Atleta
import random

class test:
    @staticmethod
    def ejectuar():
        try:
            atleta1 = Atleta("Juan")
            atleta2 = Atleta("Pedro")

            print(40*"-"+" ATLETAS "+"-"*40)
            print("Nombre: "+atleta1.mostrar_nombre())
            print(f"Destreza: {atleta1.mostrar_destreza()}")
            print(f"Energia: {atleta1.mostrar_energia()}")
            print(f"Cant Entrenamientos: {atleta1.mostrar_entrenamientos()}")

            print()

            print("Nombre: "+atleta2.mostrar_nombre())
            print(f"Destreza: {atleta2.mostrar_destreza()}")
            print(f"Energia: {atleta2.mostrar_energia()}")
            print(f"Cant Entrenamientos: {atleta2.mostrar_entrenamientos()}")

            print("-"*80)

            for i in range (40):
                num = random.randint(0,3) 
                if num == 0:
                    atleta1.entrenar()
                    print(f"Entreno atleta 1, ahora tiene {atleta1.mostrar_entrenamientos()} entrenamientos y energia {atleta1.mostrar_energia()}")
                elif num == 1:
                    atleta2.entrenar()
                    print(f"Entreno atleta 2, ahora tiene {atleta2.mostrar_entrenamientos()} entrenamientos y energia {atleta2.mostrar_energia()}")
                elif num == 2:
                    atleta1.descansar()
                    print(f"Descanso atleta 1, ahora tiene {atleta1.mostrar_energia()} energia")
                elif num == 3:
                    atleta2.descansar()
                    print(f"Descanso atleta 2, ahora tiene {atleta2.mostrar_energia()} energia")



            print(40*"-"+" FINAL "+"-"*40)
            print("Nombre: "+atleta1.mostrar_nombre())
            print(f"Destreza: {atleta1.mostrar_destreza()}")
            print(f"Energia: {atleta1.mostrar_energia()}")
            print(f"Cant Entrenamientos: {atleta1.mostrar_entrenamientos()}")

            print()

            print("Nombre: "+atleta2.mostrar_nombre())
            print(f"Destreza: {atleta2.mostrar_destreza()}")
            print(f"Energia: {atleta2.mostrar_energia()}")
            print(f"Cant Entrenamientos: {atleta2.mostrar_entrenamientos()}")

            print("-"*80)




        except TypeError as error:
            print(f"Error.{error}")
        except ValueError as error:
            print(f"Error.{error}")




if __name__ == "__main__":
    test.ejectuar()