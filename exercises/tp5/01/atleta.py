class Atleta:
    #atributos de clase
    __MAX_VALOR = 100
    __MIN_VALOR = 0 
    #atributos de instancia
    def __init__ (self, nombre:str):
        if not isinstance (nombre, str) or nombre.split() == " ":
            raise TypeError("Error. El nombre del atleta debe ser texto")
        self.__nombre = nombre
        self.__energia = Atleta.__MAX_VALOR
        self.__destreza = Atleta.__MIN_VALOR
        self.__cantidadEntrenamientos = Atleta.__MIN_VALOR


    #comandos

    def entrenar(self):
        if self.__energia - 5 < 0:
            self.__energia = Atleta.__MIN_VALOR
        else:
            self.__energia -= 5
        
        self.__cantidadEntrenamientos += 1

        if self.__cantidadEntrenamientos % 5 == 0:
            print("5 entrenamientos completados. Mejora 1 punto de destreza")
            self.__destreza += 1
        
    
    def descansar(self):
        if self.__energia + 20 > Atleta.__MAX_VALOR:
            self.__energia = Atleta.__MAX_VALOR
        else:
            self.__energia += 20


    def mostrar_nombre(self)->str:
        return self.__nombre
    def mostrar_energia(self)->int:
        return self.__energia
    def mostrar_destreza(self)->int:
        return self.__destreza
    def mostrar_entrenamientos(self)->int:
        return self.__cantidadEntrenamientos
    

    

    #consultas
    def mismaDestrezaQue(self, otroAtleta:"Atleta")->bool:
        return self.__destreza == otroAtleta.__destreza
    
    def mayorDestrezaQue(self, otroAtleta:"Atleta")->bool:
        return self.__destreza > otroAtleta.__destreza
