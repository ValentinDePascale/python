class Vinoteca:
    #atributos de clase
    __CAPACIDADMAXIMA = 5000
    def __init__(self, cantJugos:int = __CAPACIDADMAXIMA, cantBlancos:int = __CAPACIDADMAXIMA, cantTintosJovenes:int = __CAPACIDADMAXIMA, cantTintosAnejados:int = __CAPACIDADMAXIMA):
    #atributos de instancia
        self.__cantJugos = cantJugos
        self.__cantBlancos = cantBlancos
        self.__cantTintosJovenes = cantTintosJovenes
        self.__cantTintosAnejados = cantTintosAnejados  


    #comandos   
    def reponerJugos(self):
        self.__cantJugos = Vinoteca.__CAPACIDADMAXIMA
    
    def reponerVinosBlancos(self):
        self.__cantBlancos = Vinoteca.__CAPACIDADMAXIMA
    
    def reponerVinoTintoJoven(self):
        self.__cantTintosJovenes = Vinoteca.__CAPACIDADMAXIMA
    
    def reponerVinoTintoAnejado(self):
        self.__cantTintosAnejados = Vinoteca.__CAPACIDADMAXIMA
    
    def venderJugos(self, unidad:int):  
        if not isinstance (unidad, int):
            raise TypeError("Error. La cantidad de jugos debe ser entero")
        if unidad < 0:
            raise ValueError("Error. La cantidad de jugos debe ser positiva")

        if unidad > self.__cantJugos:
            resto = unidad - self.__cantJugos
            self.__cantJugos = 0
            print(f"No se pudo completar la venta. Faltan {resto} jugos")
        else:
            self.__cantJugos -= unidad

    def venderVinosBlanco(self, unidad:int):
        if not isinstance (unidad, int):
            raise TypeError("Error. La cantidad de vinos blancos debe ser entero")
        if unidad < 0:
            raise ValueError("Error. La cantidad de vinos blancos debe ser positiva")

        if unidad > self.__cantBlancos:
            resto = unidad - self.__cantBlancos
            self.__cantBlancos = 0
            print(f"No se pudo completar la venta. Faltan {resto} vinos blancos")
        else:
            self.__cantBlancos -= unidad
    
    def venderVinosTintosJovenes(self, unidad:int):
        if not isinstance (unidad, int):
            raise TypeError("Error. La cantidad de vinos tintos jovenes debe ser entero")
        if unidad < 0:
            raise ValueError("Error. La cantidad de vinos tintos jovenes debe ser positiva")
        
        if unidad > self.__cantTintosJovenes:
            resto = unidad - self.__cantTintosJovenes
            self.__cantTintosJovenes = 0
            print(f"No se pudo completar la venta. Faltan {resto} vinos tintos jovenes")
        else:
            self.__cantTintosJovenes -= unidad
        
    def venderVinosTintosAnejados(self, unidad:int):
        if not isinstance (unidad, int):
            raise TypeError("Error. La cantidad de vinos tintos anejados debe ser entero")
        if unidad < 0:
            raise ValueError("Error. La cantidad de vinos tintos anejados debe ser positiva")
        
        if unidad > self.__cantTintosAnejados:
            resto = unidad - self.__cantTintosAnejados
            self.__cantTintosAnejados = 0
            print(f"No se pudo completar la venta. Faltan {resto} vinos tintos anejados")
        else:
            self.__cantTintosAnejados -= unidad

    #consultas
    def obtenerCantidadJugos(self)->int:
        return self.__cantJugos
    
    def obtenerCantidadVinosBlancos(self)->int:
        return self.__cantBlancos
    
    def obtenerCantidadVinosTintosJovenes(self)->int:
        return self.__cantTintosJovenes
    
    def obtenerCantidadVinosTintosAnejados(self)->int:
        return self.__cantTintosAnejados
