class Automovil:
    def __init__(self, marca:str, modelo:str, anio:int, velocidadMaxima:float, velocidadActual:float):
        #validaciones de instancias
        if not isinstance (marca, str):
            raise TypeError ("Error. La marca debe ser texto.")
        if marca == "" or marca.isspace() or marca.isdigit():
            raise ValueError ("Error. Ingrese texto") 
        if not isinstance (modelo, str):
            raise TypeError ("Error. La marca debe ser texto.")
        if modelo == "" or modelo.isspace() or modelo.isdigit():
            raise ValueError ("Error. Ingrese texto") 
        if not isinstance (anio, int):
            raise TypeError("Error. El año debe ser entero")
        if anio < 0 or anio > 2025:
            raise ValueError("Error. El año debe ser positivo y menor al actual")
        if not isinstance (velocidadMaxima, float):
            raise TypeError("Error. La velocidad maxima debe ser decimal")
        if velocidadMaxima < 0:
            raise ValueError("Error. La velocidad maxima debe ser positiva")
        if not isinstance (velocidadActual, float):
            raise TypeError("Error. La velocidad actual debe ser decimal")
        if velocidadActual < 0:
            raise ValueError("Error. La velocidad actual debe ser positiva")
        if velocidadActual > velocidadMaxima:
            raise ValueError("Error. La velocidada actual debe ser menor que la maxima")
        

        #atributos de instancia 
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__velocidadMaxima = velocidadMaxima
        self.__velocidadActual = velocidadActual

    #comandos
    def establecerMarca (self, marca:str):
        if not isinstance (marca, str):
            raise TypeError("Error. La marca debe ser texto")
        if marca == "" or marca.isspace() or marca.isdigit():
            raise ValueError ("Error. Ingrese texto") 
        self.__marca = marca

    def establecerModelo (self, modelo:str):
        if not isinstance (modelo, str):
            raise TypeError("Error. El modelo debe ser texto")
        if modelo == "" or modelo.isspace() or modelo.isdigit():
            raise ValueError("Error. Ingrese texto")
        self.__modelo = modelo
    
    def establecerAnio (self, anio:int):
        if not isinstance (anio, int):
            raise TypeError("Error. El año debe ser entero")
        if anio < 0:
            raise ValueError("Error. El año debe ser positivo")
        self.__anio = anio
    
    def establecerVelocidadMaxima(self, velocidadMax:float):
        if not isinstance (velocidadMax, float):
            raise TypeError("Error. La velocidad maxima debe ser decimal")
        if velocidadMax < 0:
            raise ValueError("Error. La velocidad maxima debe ser positiva")
        self.__velocidadMaxima = velocidadMax


    def establecerVelocidadActual(self, velocidad:float):
        if not isinstance (velocidad, float):
            raise TypeError("Error. La velocidad actual debe ser decimal")
        if velocidad < 0:
            raise ValueError("Error. La velocidad actual debe ser positiva")
        if velocidad > velocidad:
            raise ValueError("Error. La velocidada actual debe ser menor que la maxima")
        self.__velocidadActual = velocidad

    def acelerar(self, incrementoVelocidad:int):
        if not isinstance (incrementoVelocidad, int):
            raise TypeError("Error. El incremento de velocidad debe ser entero")
        if incrementoVelocidad < 0:
            raise ValueError("Error. El incremento de velocidad no puede ser menor a 0")
        self.__velocidadActual = self.__velocidadActual + incrementoVelocidad
        if self.__velocidadActual > self.__velocidadMaxima:
            print (f"Se alcanzo la velocidad maxima {self.__velocidadMaxima} km")
            self.__velocidadActual = self.__velocidadMaxima
    
    def desacelerar(self, decrementoVelocidad:int):
        if not isinstance(decrementoVelocidad, int):
            raise TypeError("Error. El decremento de velocidad debe ser entero  ")
        if decrementoVelocidad <= 0:
            raise ValueError("Erro. El decremento de velocidad no debe ser menor o igual a 0")
        self.__velocidadActual = self.__velocidadActual - decrementoVelocidad 
        if self.__velocidadActual < 0:
            print(f"Se detuvo el auto x completo. Velocidad 0")   
            self.__velocidadActual = 0       

    def frenarPorCompleto(self):
        self.__velocidadActual = 0

    #consultas
    def obtenerMarca(self)->str:
        return self.__marca
    
    def obtenerModelo(self)->str:
        return self.__modelo
    
    def obtenerAnio(self)->int:
        return self.__anio
    
    def obtenerVelocidadMaxima(self)->float:
        return self.__velocidadMaxima
    
    def obtenerVelocidadActual(self)->float:
        return self.__velocidadActual
    
    def calcularMinutosParaLlegar(self, distanciaKM:float)->int:
        if not isinstance(distanciaKM, (float, int)):
            raise TypeError("Error. La distancia debe ser decimal")
        if distanciaKM <= 0:
            raise ValueError("Error. La distancia debe ser positiva")
        if self.__velocidadActual == 0:
            raise ValueError("Error. El auto debe estar en movinmineto para calcular la velocidad.")
        
        return round((distanciaKM / self.__velocidadActual) * 60, 2)
    
