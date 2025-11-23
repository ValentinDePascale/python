from modelos.entidades.libro import Libro
import json

class RepositorioLibro:
    __RUTA_ARCHIVO = "datos\libros.json"


    def __init__(self):
        self.__libros = []
        self.__cargarDesdeArchivos()


    def __cargarDesdeArchivos(self):
        try:
            with open(self.__RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                datos_cargados = json.load(archivo)
                for libro in datos_cargados:
                    self.__libros.append(Libro.fromDiccionario(libro))
        except FileNotFoundError:
            print("El archivo de datos no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar los datos desde el archivo: {e}")


    def __guardarEnArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                datos_a_guardar = []
                for tema in self.__libros:
                    datos_a_guardar.append(tema.toDiccionario())
                json.dump(datos_a_guardar, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")

    #GET ALL
    def obtener_todos(self):
        return self.__libros
    
    #GET individual
    def obtener_libro_isbn(self, isbn:str)->Libro | None :
        if not isinstance(isbn, str) or isbn.strip() == "" or isbn.isspace():
            raise ValueError("El IBSN debe ser una cadena no vacía.")
        for l in self.__libros:
            if l.obtenerISBN() == isbn:
                return l
        return None
    

    def existe_isbn(self, isbn:str)->bool:
        if not isinstance(isbn, str) or isbn.strip() == "" or isbn.isspace():
            raise ValueError("El IBSN debe ser una cadena no vacía.")
        
        for l in self.__libros:
            if l.obtenerISBN() == isbn:
                return True
        return False
    
    def existe_libro(self, otroLibro:Libro)->bool:
        if not isinstance(otroLibro, Libro):
            raise ValueError("El libro debe se instancia Libro")

        for l in self.__libros:
            if l == otroLibro:
                return True
            
        return False
    
    #PUT NO NECESARIO

    def modificar(self, isbn:str, dict_libro:dict)->bool:

        libroAModificar = self.obtener_libro_isbn(isbn)
        if libroAModificar:
            if "titulo" in dict_libro:
                libroAModificar.establecerTitulo(dict_libro["titulo"])
            if "autor" in dict_libro:
                libroAModificar.estabecerAutor(dict_libro["autor"])
            if "genero" in dict_libro:
                libroAModificar.estabecerGenero(dict_libro["genero"])
            if "anio_publicacion" in dict_libro:
                libroAModificar.estabeceAnioPublicacion(dict_libro["anio_publicacion"])
            self.__guardarEnArchivo()
            return True
        return False
        
        
    
    #POST agregar
    def agregar_libro(self, nuevoLibro:Libro)->bool:
        if not isinstance(nuevoLibro, Libro):
            raise Exception("Se esperaba un libro de tipo Libro")
        if not self.existe_libro(nuevoLibro):
            self.__libros.append(nuevoLibro)
            self.__guardarEnArchivo()
            return True
        return False
    
    #DELETE isbn
    def eliminar_libro_isbn(self, isbn:str)->bool:
        if not isinstance(isbn, str) or isbn.strip() == "" or isbn.isspace():
            raise ValueError("El IBSN debe ser una cadena no vacía.")
        
        for l in self.__libros:
            if l.obtenerISBN() == isbn:
                self.__libros.remove(l)
                self.__guardarEnArchivo()
                return True
        return False
