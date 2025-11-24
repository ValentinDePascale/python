from datetime import date

class Prestamo:
    __ULITMOID = 0

    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        if not isinstance(diccionario, dict):
            raise ValueError("Se esperaba diccionario instancia de dict")
        
        if not "id" in diccionario or "socio_id" in diccionario or "libro_isbn" in diccionario or "fecha_retiro" in diccionario or "cant_dias" in diccionario or "fecha_devolucion" in diccionario:
            raise Exception("El diccionario debe contener: 'id', 'socio_dni', 'libro_isbn', 'fecha_retiro', 'cant_dias', 'fecha_devolucion'")

        return cls(
            id = diccionario["id"],
            socio_id = diccionario["socio_id"],
            libro_isbn = diccionario["libro_isbn"],
            fecha_retiro = diccionario["fecha_retiro"],
            cant_dias = diccionario["cant_dias"],
            fecha_devolucion = diccionario["fecha_devolucion"]

        )

    @classmethod
    def obtenerNuevoId(cls)->int:
        cls.__ULITMOID += 1 
        return cls.__ULITMOID

    @classmethod
    def establecerUltimoId(cls, ultimo_id:int):
        if isinstance(ultimo_id, int):
            raise ValueError("EL ultimo id debe ser entero positivo")
        cls.__ULITMOID = ultimo_id

    def __init__(self, id:int, socio_dni:int, libro_isbn:str, fecha_retiro:date, cant_dias:int):

        if not isinstance(id, int) or id <= 0:
            raise ValueError("El id debe ser un entero positivo")
        if not isinstance(socio_dni, int) or socio_dni <= 0:
            raise ValueError("El dni del socio debe ser un entero positivo")
        if not isinstance(libro_isbn, str) or libro_isbn.strip() == "" or libro_isbn.isspace():
            raise ValueError("El IBSN debe ser una cadena no vacía.")
        if not isinstance(fecha_retiro, date):
            raise ValueError("La fecha de retiro debe ser una fecha valida")
        if not isinstance(cant_dias, int) or cant_dias <= 0:
            raise ValueError("La cantidad de dias debe ser un entero positivo")
        
        self.__id = id
        self.__socio_dni = socio_dni
        self.__libro_isbn = libro_isbn
        self.__fecha_retiro = fecha_retiro
        self.__cant_dias = cant_dias
        self.__fecha_devolucion = None

    def obtenerId(self)->int:
        return self.__id
    
    def obtenerSocioDNI(self)->int:
        return self.__socio_dni
    
    def obtenerISBN(self)->str:
        return self.__libro_isbn
    
    def obtenerFechaRetiro(self)->date:
        return self.__fecha_retiro
    
    def obtenerCantDias(self)->int:
        return self.__cant_dias
    
    def obtenerFechaDevolucion(self)->date:
        return self.__fecha_devolucion
    
    def establecerSocioDNI(self, dni:int):
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("El id del socio debe ser un entero positivo")
        self.__socio_dni = dni

    def establecerISBN(self, isbn:str):
        if not isinstance(isbn, str) or isbn.strip() == "" or isbn.isspace():
            raise ValueError("El IBSN debe ser una cadena no vacía.")
        self.__libro_isbn = isbn

    def establecerFechaRetiro(self, fecha_retiro:date):
        if not isinstance(fecha_retiro, date):
            raise ValueError("La fecha de retiro debe ser una fecha valida")
        self.__fecha_retiro = fecha_retiro

    def estalecerCantDias(self, cant_dias:int):
        if not isinstance(cant_dias, int) or cant_dias <= 0:
            raise ValueError("La cantidad de dias debe ser un entero positivo")
        self.__cant_dias = cant_dias    


    def establecerFechaDevolucion(self, fecha_devolucion:date):
        if not isinstance(fecha_devolucion, date):
            raise ValueError("La fecha de devolucion debe ser una fecha valida")
        self.__fecha_devolucion = fecha_devolucion

    def esIgual(self, otroPrestamo:"Prestamo")->bool:
        if not isinstance( otroPrestamo, Prestamo):
            raise ValueError("El parametro debe ser un objeto de la clase Prestamo")
        return self.__id == otroPrestamo.obtenerId()


    def __str__(self)->str:
        return f"Prestamo[ID: {self.__id}, Socio DNI: {self.__socio_dni}, Libro ISBN: {self.__libro_isbn}, Fecha Retiro: {self.__fecha_retiro}, Cantidad Dias: {self.__cant_dias}, Fecha Devolucion: {self.__fecha_devolucion}]"
    
    def toDiccioanrio(self)->dict:
        return {
            "id": self.__id,
            "socio_dni": self.__socio_dni,
            "libro_isbn": self.__libro_isbn,
            "fecha_retiro": self.__fecha_retiro,
            "cant_dias": self.__cant_dias,
            "fecha_devolucion": self.__fecha_devolucion

        }
