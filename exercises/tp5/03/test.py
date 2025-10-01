from color import Color
import random

class Test:
    @staticmethod
    def ejecutar():
        color1 = Color() #vacio (blanco)
        color2 = Color(255, 0, 0) #rojo
        color3 = Color(0, 0, 0) #negro
        color4 = Color(140, 33, 12) #random
        color5 = Color(50, 50, 50) #gris

        separador = ("-"*30)
        print(separador+" COLORES "+separador)
        print(f"Color 1: {color1.obtener_rojo()}, {color1.obtener_azul()}, {color1.obtener_verde()}")
        print(f"Color 2: {color2.obtener_rojo()}, {color2.obtener_azul()}, {color2.obtener_verde()}")
        print(f"Color 3: {color3.obtener_rojo()}, {color3.obtener_azul()}, {color3.obtener_verde()}")
        print(f"Color 4: {color4.obtener_rojo()}, {color4.obtener_azul()}, {color4.obtener_verde()}")
        print(f"Color 5: {color5.obtener_rojo()}, {color5.obtener_azul()}, {color5.obtener_verde()}")

        print(separador*2)

        if color1.esRojo == True:
            print("El color 1 es rojo")
        else:
            print("El color 1 no es rojo")
        
        if color2.esRojo:
            print("El color 2 es rojo")
        else:
            print("El color 2 no es rojo")

        if color3.esNegro:
            print("El color 3 es negro")
        else:
            print("El color 3 no es negro")

        if color5.esGris:
            print("El color 5 es gris")
        else:
            print("El color 5 no es gris")

        print(separador*2)


        print("Variando color 4....")
        color4.variar_rojo(random.randrange(0,255))
        color4.variar_azul(random.randrange(0,255))
        color4.variar_verde(random.randrange(0,255))

        print("Los nuevos valores de color 4 son: ")
        print(f"Color 4: {color4.obtener_rojo()}, {color4.obtener_azul()}, {color4.obtener_verde()}")

        print(separador*2)

        complementode5 = color5.complemento()
        print(f"El complemento de 5 es: {complementode5.obtener_rojo()}, {complementode5.obtener_azul()}, {complementode5.obtener_verde()}")   

        print(separador*2)

        print("Clonando color 5...")
        color6 = color5.clonar()

        print("Copiando color 4 en color 3...")
        color4.copiar(color3)

        print(separador*2)

        if color1.esIgualQue(color3):
            print("Color 1 y color 3 son iguales")
        else:
            print("Color 1 y color 3 son distintos")

        if color5.esIgualQue(color6) == True:
            print("Color 5 y color 6 son iguales")
        else:
            print("Color 5 y color 6 son distintos")

        print(separador+" COLORES "+separador)
        print(f"Color 1: {color1.obtener_rojo()}, {color1.obtener_azul()}, {color1.obtener_verde()}")
        print(f"Color 2: {color2.obtener_rojo()}, {color2.obtener_azul()}, {color2.obtener_verde()}")
        print(f"Color 3: {color3.obtener_rojo()}, {color3.obtener_azul()}, {color3.obtener_verde()}")
        print(f"Color 4: {color4.obtener_rojo()}, {color4.obtener_azul()}, {color4.obtener_verde()}")
        print(f"Color 5: {color5.obtener_rojo()}, {color5.obtener_azul()}, {color5.obtener_verde()}")
        print(f"Color complemento 5: {complementode5.obtener_rojo()}, {complementode5.obtener_azul()}, {complementode5.obtener_verde()}")   
        print(f"Color 6: {color6.obtener_rojo()}, {color6.obtener_azul()}, {color6.obtener_verde()}")


        

if __name__ == "__main__":
    Test.ejecutar()