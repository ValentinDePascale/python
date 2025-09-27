class Repartidor:
    #atributos de clase
    __valorKm = 0
    __valorKmExtra = 0

    #atributos de instancia
    def __init__(self, nombre:str, edad:int, cobros:list, pedidosEntregados:int = 0):
        if cobros is None:
            cobros = []
        pass
        self.__nombre = nombre
        self.__edad = edad
        self.__cobros = []  
        self.__pedidosEntregados = pedidosEntregados


    #comandos
    def calcularViaje(self, km:float, propina=float=0)->float:
        Repartidor.__valorKm = km * 500
        if km > 3:
            Repartidor.__valorKmExtra = (km-3) * 100
        return Repartidor.__valorKm + Repartidor.__valorKmExtra + propina



    def hacerViaje(self, km:float, propina:float=0):
 
        dineroViaje = self.calcularViaje(km, propina)
        self.__cobros.append(dineroViaje)
        self.__pedidosEntregados += 1


    #consutas
    def obtenerNombre(self)->str:
        return self.__nombre

    def obtenerEdad(self)->int:
        return self.__edad
    
    def obtenerPedidosEntregados(self)->int:
        return self.__pedidosEntregados

    def obtenerRecaudado(self)->float:
        for i in self.__cobros:
            suma += i
        return suma
