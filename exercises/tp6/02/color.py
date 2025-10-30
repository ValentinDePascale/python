class Color:
    #atributos de instancia
    def __init__(self, rojo:int = "255", verde:int = "255", azul:int = "255"):
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul



    #comandos

    def variar(self, valor:int):
        if not isinstance (valor, int) or valor < 0 or valor > 255:
            raise ValueError("Error. Ingrese el valor que va a sumar en entero")
        self.variar_rojo(valor)
        self.variar_azul(valor)
        self.variar_verde(valor)

    def variar_rojo(self, valor:int):
        if not isinstance (valor, int) or valor < 0 or valor > 255:
            raise ValueError("Error. Ingrese el valor que va a sumar en entero")
        if self.__rojo + valor >= 255:
            self.__rojo = 255
            print("Se llego al limite. El color rojo se establecio en 255")
        else: 
            self.__rojo += valor 

    def variar_azul(self, valor:int):
        if not isinstance (valor, int) or valor < 0 or valor > 255:
            raise ValueError("Error. Ingrese el valor que va a sumar en entero")
        if self.__azul + valor >= 255:
            self.__azul = 255
            print("Se llego al limite. El color azul se establecio en 255")
        else: 
            self.__azul += valor
    
    def variar_verde(self, valor:int):
        if not isinstance (valor, int) or valor < 0 or valor > 255:
            raise ValueError("Error. Ingrese el valor que va a sumar en entero")
        if self.__verde + valor >= 255:
            self.__verde = 255
            print("Se llego al limite. El color verde se establecio en 255")
        else: 
            self.__verde += valor 
        
    def establecer_rojo(self, valor:int):
        if not isinstance (valor, int) or valor < 0 or valor > 255:
            raise ValueError("Error. Ingrese el valor que le va a establecer a rojo como entero")
        self.__rojo = valor

    def establecer_azul(self, valor:int):
        if not isinstance (valor, int) or valor < 0 or valor > 255:
            raise ValueError("Error. Ingrese el valor que le va a establecer a azul como entero")
        self.__azul = valor

    def establecer_verde(self, valor:int):
        if not isinstance (valor, int) or valor < 0 or valor > 255:
            raise ValueError("Error. Ingrese el valor que le va a establecer a verde como entero")
        self.__verde = valor
    

    def copiar(self, otroColor: "Color"):
        if not isinstance(otroColor, Color):
            raise ValueError("Error. El color que va a copiar no es valido")
        self.__rojo = otroColor.obtener_rojo()
        self.__verde = otroColor.obtener_verde()
        self.__azul = otroColor.obtener_azul()



    #consultas

    def obtener_rojo(self)->int:
        return self.__rojo
    
    def obtener_azul(self)->int:
        return self.__azul
    
    def obtener_verde(self)->int:
        return self.__verde
    
    def esRojo(self)->bool:
        return self.__rojo == 255 and self.__azul == 0 and self.__verde == 0
        
    def esNegro(self)->bool:
        return self.__rojo == 0 and self.__azul == 0 and self.__verde == 0

    def esGris(self)->bool:
        return self.__rojo == 50 and self.__azul == 50 and self.__verde == 50     

    def complemento(self)->"Color":
        complementoRojo = 255 - self.__rojo
        complementoAzul = 255 - self.__azul
        complementoVerde = 255 - self.__verde
        complemento = Color(complementoRojo, complementoAzul, complementoVerde)
        return complemento
    
    def esIgualQue(self, otroColor:"Color")->bool:
        if not isinstance(otroColor, Color):
            raise ValueError("Error. El color que desea comparar no es valido")
        return (self.__rojo == otroColor.obtener_rojo() and self.__azul == otroColor.obtener_azul() and self.__verde == otroColor.obtener_verde() )
    
    def clonar(self)-> "Color":
        colorClonado = Color(self.__rojo, self.__verde, self.__azul)
        return colorClonado