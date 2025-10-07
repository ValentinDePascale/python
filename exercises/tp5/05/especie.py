class Especie:
    def __init__(self, nombre:str):

        if not isinstance(nombre, str):
            raise TypeError("Error. El nombre debe ser texto")
        if nombre == "" or nombre.isspace()
            raise ValueError("Error. El nombre no debe tener espacios ni ser vacio")

        self.__nombre = nombre
        self.__machos = 0
        self.__hembras = 0
        self.__ritmo= 0.0


    #Comandos

    def establecerHembras(self, cantHembras:int):
        if not isinstance(cantHembras, int):
            raise TypeError("Error. La cantidad de hembras deben ser entero")
        if cantHembras < 0:
            raise ValueError("Error. La cantidad de hembras debe ser un numero positivo")

        self.__hembras = cantHembras

    def establecerMachos(self, cantMachos:int):
        if not isinstance(cantMachos, int):
            raise TypeError("Error. La cantidad de machos deben ser entero")
        if cantMachos < 0:
            raise ValueError("Error. La cantidad de machos debe ser un numero positivo")

        self.__machos = cantMachos

    def estableceRitmo(self, valorRitmo:float):
        if not isinstance(valorRitmo, float):
            raise TypeError("Error. El ritmo debe ser real")
        if valorRitmo < 0:
            raise ValueError("Error. El ritmo debe ser un numero positivo")

        self.__ritmo = valorRitmo

    def actualizarHembras(self, cantHembras:int):
        if not isinstance(cantHembras, int):
            raise TypeError("Error. La cantidad de hembras que desea actualizar debe ser entero")
        if self.__hembras + cantHembras < 0:
            self.__hembras = 0
            print("El valor de las hembras es 0")
        else:
            self.__hembras += cantHembras

    def actualizarMachos(self, cantMachos:int):
        if not isinstance(cantMachos, int):
            raise TypeError("Error. La cantidad de machos que desea actualizar debe ser entero")
        if self.__machos + cantMachos < 0:
            self.__machos = 0
            print("El valor de los machos es 0")
        else:
            self.__machos += cantMachos

    def actualizarRitmo(self, valorRitmo:int):
        if not isinstance(valorRitmo, int):
            raise TypeError("Error. El valor ritmo desea actualizar debe ser entero")
        if self.__ritmo + valorRitmo < 0:
            self.__ritmo = 0
            print("El valor del ritmo es 0")
        else:
            self.__ritmo += valorRitmo


    #Consultas
    def obtenerHembras (self):
        return self.__hembras
    
    def obtenerMachos (self):
        
        return self.__machos
    
    def obtenerRitmo (self):
        return self.__ritmo

    def poblacionActual(self)->int:
        return self.__hembras + self.__machos
    
    def poblacionEstimada(self, anio:int)->int:
        poblacion = self.__poblacionActual()
        for i in range (anio):
            poblacion = poblacion * self.__ritmo
        if poblacion < 0:
            poblacion
        return int(poblacion)
    
    def aniosParaPoblacion(poblacion:int)->int:
        
