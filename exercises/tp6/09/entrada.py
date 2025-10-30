from visitante import Visitante
class Entrada:
    def __init__(self, numero:int, fecha:str, tipo:str):

        if not isinstance(fecha, str) or fecha.isspace() or fecha.strip() == "":
            raise ValueError("La fech debe ser un string")


        if not isinstance(tipo, str) or tipo.isspace() or tipo.strip() == "":
            raise ValueError("El tipo debe ser un string")

        self.__numero = numero
        self.__fecha = fecha
        self.__tipo = tipo
        self.__visitante = None


    def asignarEntrada(self, visitante:"Visitante"):
        if self.__visitante == None: 
            if visitante.visitanteTieneEntrada() == False:
                self.__visitante = visitante
                visitante.entradaAsignada()
            else:
                print(f"El visitante {visitante.obtenerNombre()} ya tiene entrada")
        else:
            print(f"La entrada ya fue asignada a otro visitante")



    def __str__(self):
        return (f"Numero: {self.__numero}, Fecha: {self.__fecha}, Tipo: {self.__tipo}")