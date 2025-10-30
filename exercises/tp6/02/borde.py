from color import Color

class Borde:
    def __init__(self, grosor:int, color:"Color"):
        if not isinstance(grosor, int) or grosor < 0:
            raise ValueError("El grosor del borde debe ser entero positivo")  
        if not isinstance(color, Color):
            raise TypeError("El color debe ser instancia de color")
        
        self.__grosor = grosor
        self.__color = color

    def __str__(self):
        return (f"Grosor del borde: {self.__grosor} \n"
                f"Color del borde: {self.__color.obtener_rojo()}, {self.__color.obtener_verde()}, {self.__color.obtener_azul()}"
        )
    

    def copiarValores(self, otroBorde:"Borde"):
        self.__grosor = otroBorde.obtenerBorde()
        self.__color = otroBorde.obtenerColor()

    def obtenerBorde(self)->int:
        return self.__grosor


    def obtenerColor(self)->"Color":
        return self.__color
    
    def clonar(self)->"Borde":
        bordeClonado = Borde(self.__grosor, self.__color)
        return bordeClonado
    
    def esIgualQue(self, otroBorde:"Borde")->bool:
        if self.__grosor == otroBorde.obtenerBorde() and self.__color == otroBorde.obtenerColor():
            return True
        else:
            return False


# class test:
#     def run():
#         color1 = Color(100,100,100)
#         color2 = Color(20, 20, 20)
#         borde1 = Borde(1, color1)
#         borde2 = Borde(3, color2)
#         borde3 = borde1.clonar()
#         print(borde1)
#         print(borde2)

#         borde1.copiarValores(borde2)

#         print(borde1)

#         print(borde3)

#         if borde1.esIgualQue(borde2):
#             print("borde 1 es igual q borde 2")
#         else:
#             print("no es igual")

# if __name__ == "__main__":
#     test.run()