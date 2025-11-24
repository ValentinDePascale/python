from modelos.entidades.prestamos import Prestamo
from modelos.repositorios.repositorio_libro import RepositorioLibro
import json
from datetime import date


class RepositorioPrestamos:

    __RUTA_ARCHIVO = "datos/prestamos.json"

    def __init__(self):
        self.__prestamos = []
        self.__repo_libros = RepositorioLibro()
        self.__cargarTodos()

    
    def __cargarTodos(self):
        try:
            with open(self.__RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                datos_cargados = json.load(archivo)
                for prestamo in datos_cargados:
                    self.__prestamos.append(Prestamo.fromDiccionario(prestamo))
        except FileNotFoundError:
            print("El archivo de datos no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar los datos desde el archivo: {e}")


    def _guardarTodos(self):
        try:
            with open(self.__RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                datos_a_guardar = []
                for prestamo in self.__prestamos:
                    datos_a_guardar.append(prestamo.toDiccionario())
                json.dump(datos_a_guardar, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")

        
    def estaDevuelto(self, prestamoAVerificar:Prestamo)->bool:
        if prestamoAVerificar.obtenerFechaDevolucion() is not None:
            return True
        
        return False
    
    

    def cantidadLibrosSinDevolver(self, isbn:str)->int:
        if not isinstance(isbn, str) or isbn.strip() == "" or isbn.isspace():
            raise ValueError("El IBSN debe ser una cadena no vacía.")
        
        contador = 0
        for prestamo in self.__prestamos:
            if prestamo.obtenerISBN() == isbn and prestamo.obtenerFechaDevolucion() is None:
                contador += 1
        return contador
    

    def existe(self, socio_dni:int, libro_isbn:str, fecha_retiro:date)->bool:
        if not isinstance (socio_dni, int) or socio_dni <= 0:
            raise ValueError("El dni del socio debe ser un entero positivo")
        if not isinstance(libro_isbn, str) or libro_isbn.strip() == "" or libro_isbn.isspace():
            raise ValueError("El IBSN debe ser una cadena no vacía.")
        if not isinstance(fecha_retiro, date):
            raise ValueError("La fecha de retiro debe ser una fecha valida")
        

        for p in self.__prestamos:
            if p.obtenerSocioDNI() == socio_dni and p.obtenerISBN() == libro_isbn and p.obtenerFechaRetiro() == fecha_retiro:
                return True
        return False
    
    def obtenerPrestamoId(self, id:int)->Prestamo | None:
        if not isinstance(id, int):
            raise ValueError("El Id debe ser entero positivo")
        
        for p in self.__prestamos:
            if p.obtenerId() == id:
                return p
        return None


    #GET ALL
    def obtenerTodos(self)-> list [Prestamo]:
        return self.__prestamos
    

    #GET Prestamo x id, isbn, fecha_retiro

    def obtenerPrestamo(self, socio_dni:int, libro_isbn:str, fecha_retiro:date)-> Prestamo | None:
        if not isinstance (socio_dni, int) or socio_dni <= 0:
            raise ValueError("El dni del socio debe ser un entero positivo")
        if not isinstance(libro_isbn, str) or libro_isbn.strip() == "" or libro_isbn.isspace():
            raise ValueError("El IBSN debe ser una cadena no vacía.")
        if not isinstance(fecha_retiro, date):
            raise ValueError("La fecha de retiro debe ser una fecha valida")
        
        for p in self.__prestamos:
            if p.obtenerSocioDNI() == socio_dni and p.obtenerISBN() == libro_isbn and p.obtenerFechaRetiro() == fecha_retiro:
                return p
        return None

    

    #POST AGREGAR 
    def agregar(self, nuevoPrestamo:Prestamo):
        if not isinstance(nuevoPrestamo, Prestamo):
            raise ValueError("El prestamo debe ser instancia de prestamo")
        
        isbn_libro_a_prestar = nuevoPrestamo.obtenerISBN()
        socio_dni = nuevoPrestamo.obtenerSocioDNI()
        fecha_retiro = nuevoPrestamo.obtenerFechaRetiro()

        if not self.existe(socio_dni, isbn_libro_a_prestar, fecha_retiro):
            
            cant_prestamos_activos = self.cantidadLibrosSinDevolver(isbn_libro_a_prestar)
            
            libro_a_prestar = self.__repo_libros.obtener_libro_isbn(isbn_libro_a_prestar)

            if libro_a_prestar is None:
                raise Exception(f"El libro con ISBN {isbn_libro_a_prestar} no existe.")
            
            if (libro_a_prestar.obtenerCantidadEjemplares() - cant_prestamos_activos) >= 1:
                
                nuevoPrestamo.establecerId(RepositorioPrestamos.obtenerNuevoID())
                
                self.__prestamos.append(nuevoPrestamo)
                self._guardarTodos()
            else:
                raise Exception("El libro solicitado no tiene ejemplares dispoibles para prestar")
        else:
            raise Exception("El prestamo ya fue agregado")
        
    #PUT MODIFICAR
    def modificarPorID(self, id:int, dict_prestamo:dict)->bool:
        prestamoAModificar = self.obtenerPrestamoId(id)
        if prestamoAModificar:
            if "socio_dni" in dict_prestamo:
                if not isinstance(dict_prestamo["socio_dni"], int) or dict_prestamo["socio_dni"] <= 0:
                    raise ValueError("El dni del socio debe ser un entero positivo")
                prestamoAModificar.establecerSocioDNI(dict_prestamo["socio_dni"])
            if "libro_isbn" in dict_prestamo:
                if not isinstance(dict_prestamo["libro_isbn"], str) or dict_prestamo["libro_isbn"].strip() == "" or dict_prestamo["libro_isbn"].isspace():
                    raise ValueError("El IBSN debe ser una cadena no vacía.")
                prestamoAModificar.establecerISBN(dict_prestamo["libro_isbn"])
            if "fecha_retiro" in dict_prestamo:
                if not isinstance(dict_prestamo["fecha_retiro"], date):
                    raise ValueError("La fecha de retiro debe ser una fecha valida")
                prestamoAModificar.establecerFechaRetiro(dict_prestamo["fecha_retiro"])
            if "cant_dias" in dict_prestamo:
                if not isinstance(dict_prestamo["cant_dias"], int) or dict_prestamo["cant_dias"] <= 0:
                    raise ValueError("La cantidad de dias debe ser un entero positivo")
                prestamoAModificar.estalecerCantDias(dict_prestamo["cant_dias"])
            if "fecha_devolucion" in dict_prestamo:
                if not isinstance(dict_prestamo["fecha_devolucion"], date):
                    raise ValueError("La fecha de devolucion debe ser una fecha valida")
                prestamoAModificar.establecerFechaDevolucion(dict_prestamo["fecha_devolucion"])
            self._guardarTodos()
            return True
        return False
    
    #DELETE x ID

    def eliminarID(self, id:int)->bool:
        prestamoAEliminar = self.obtenerPrestamoId(id)

        if prestamoAEliminar:
            self.__prestamos.remove(prestamoAEliminar)
            self._guardarTodos()
            return True
        return False

    


