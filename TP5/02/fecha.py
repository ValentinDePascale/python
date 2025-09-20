class Fecha:
    #atributos de instancia
    def __init__(self, dia:int, mes:int, anio:int):
        self.__anio = anio
        self.__mes = mes
        self.__dia = dia
        
    #constructor
    def establecerDia(self, dia:int):
        cantdias = Fecha.__diasDelMes
        if dia > cantdias or dia < 0:
            raise ValueError(f"Error. El dia sobrepasa a la cantidad de dias {cantdias}")
        self.__dia = dia
    
    def establecerMes(self, mes:int):
        if mes < 0 and mes > 12:
            raise ValueError("Error. Ingrese Mes entre 0 y 12")
        
        self.__mes = mes
    
    def establecerAnio(self, anio:int):
        if not isinstance(anio, int):
            raise TypeError("Error. El año debe ser entero")
        if anio < 0:
            raise ValueError("Error. Año debe ser positivo")
        self.__anio = anio


    #consultas
    def obtenerDia(self)->int:
        return self.__dia
    
    def obtenerMes(self)->int:
        return self.__mes
    
    def obtenerAnio(self)->int:
        return self.__anio
    


    def esAnterior(self, otraFecha: "Fecha")->bool:
        diaObjeto = self.__dia
        mesObjeto = self.__mes
        anioObjeto = self.__anio

        return (diaObjeto, mesObjeto, anioObjeto) < (otraFecha.obtenerDia(), otraFecha.obtenerMes(), otraFecha.obtenerAnio())
    
    def sumaDias(self, cantDias:int)-> "Fecha":
        dia = self.__dia
        mes = self.__mes
        anio = self.__anio

        for i in range (cantDias):
            dia += 1
            cantDiasMes = Fecha.__diasDelMes(mes, anio)

            if dia > cantDiasMes:
                mes += 1
                dia = 1
                if mes > 12:
                    anio += 1
                    mes = 1
                    dia = 1

        return Fecha(dia, mes, anio)

    def diaSiguiente(self)->"Fecha":
        dia = self.__dia
        mes = self.__mes
        anio = self.__anio
        
        cantDiasMes = Fecha.__diasDelMes(mes, anio)
        dia += 1
        if dia > cantDiasMes:
            mes += 1
            dia = 1
            if mes > 12:
                anio += 1
                mes = 1
                dia = 1

        return Fecha(dia, mes, anio)
    
    def esIgualQue(self, otraFecha: "Fecha")->bool:
        dia = self.__dia
        mes = self.__mes
        anio = self.__anio
        return (dia, mes, anio) == (otraFecha.obtenerDia(), otraFecha.obtenerMes(), otraFecha.obtenerAnio())

    @staticmethod
    def __esBisiesto(anio:int)->bool:
        esBisiesto = False
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            esBisiesto = True
        return esBisiesto
        
    @staticmethod    
    def __diasDelMes(mes:int, anio:int)->int:
        dias = 0
        if mes in (1,3,5,7,8,10,12):
            dias = 31
        elif mes in (4,6,9,11):
            dias = 30
        else:
            if Fecha.__esBisiesto(anio):
                dias = 29
            else:
                dias = 28
        return dias
        