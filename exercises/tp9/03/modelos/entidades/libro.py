class Libro:
    
    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        if not isinstance(diccionario, dict):
            raise ValueError("El argumento debe ser un diccionario")
        if "ISBN" not in diccionario or "titulo" not in diccionario or "autor" not in diccionario or "genero" not in diccionario or "anio_publicacion" not in diccionario:
            raise ValueError("El diccionario debe contener las claves 'ISBN', 'titulo', 'autor', 'genero' y 'anio_publicacion'")
        
        return cls(
            ISBN = diccionario["ISBN"],
            titulo = diccionario["titulo"],
            autor = diccionario["autor"],
            genero = diccionario["genero"],
            anio_publicacion = diccionario["anio_publicacion"]
        )
    
    def __init__(self, ISBN:str, titulo:str, autor:str, genero:str, anio_publicacion:int):
        if not isinstance(ISBN, str) or ISBN.strip() == "" or ISBN.isspace():
            raise ValueError("El ISBN debe ser una cadena no vacía.")
        if not isinstance(titulo, str) or titulo.strip() == "" or titulo.isspace():
            raise ValueError("El título debe ser una cadena no vacía.")
        if not isinstance(autor, str) or autor.strip() == "" or autor.isspace():
            raise ValueError("El autor debe ser una cadena no vacía.")
        if not isinstance(genero, str) or genero.strip() == "" or genero.isspace():
            raise ValueError("El género debe ser una cadena no vacía.")
        if not isinstance(anio_publicacion, int) or anio_publicacion <= 0:
            raise ValueError("El año de publicación debe ser un entero positivo.")


        self.__ISBN = ISBN
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio_publicacion = anio_publicacion
        self.__cantidad_ejemplares = 0


    def obtenerISBN(self)->str:
        return self.__ISBN
    
    def obtenerTitulo(self)->str:
        return self.__titulo
        
    def obtenerAutor(self)->str:
        return self.__autor
        
    def obtenerGenero(self)->str:
        return self.__genero   
        
    def obtenerAnioPublicacion(self)->int:
        return self.__anio_publicacion

    def obtenerCantidadEjemplares(self)->int:
        return self.__cantidad_ejemplares
        
    def establecerISBN(self, ISBN:str):
        if not isinstance(ISBN, str) or ISBN.strip() == "" or ISBN.isspace():
            raise ValueError("El IBSN debe ser una cadena no vacía.")
        self.__ISBN = ISBN

    def establecerTitulo(self, titulo:str):
        if not isinstance(titulo, str) or titulo.strip() == "" or titulo.isspace():
            raise ValueError("El título debe ser una cadena no vacía.")
        self.__titulo = titulo

    def establecerAutor(self, autor:str):
        if not isinstance(autor, str) or autor.strip() == "" or autor.isspace():
            raise ValueError("El autor debe ser una cadena no vacía.")
        self.__autor = autor

    def establecerGenero(self, genero:str):
        if not isinstance(genero, str) or genero.strip() == "" or genero.isspace():
            raise ValueError("El género debe ser una cadena no vacía.")
        self.__genero = genero

    def establecerAnioPublicacion(self, anio_publicacion:int):
        if not isinstance(anio_publicacion, int) or anio_publicacion <= 0:
            raise ValueError("El año de publicación debe ser un entero positivo.")
        self.__anio_publicacion = anio_publicacion 

    def establecerCantidadEjemplares(self, cantidad_ejemplares:int):
        if not isinstance(cantidad_ejemplares, int) or cantidad_ejemplares < 0:
            raise ValueError("La cantidad de ejemplares debe ser un entero no negativo.")
        self.__cantidad_ejemplares = cantidad_ejemplares


    def esIgual(self, otroLibro)->bool:
        if not isinstance(otroLibro, Libro):
            raise ValueError("El argumento debe ser una instancia de Libro.")
    
        return self.__ISBN == otroLibro.obtenerIBSN()
        

    def toDiccionario(self)->dict:
        return {
            "ISBN": self.__ISBN,
            "titulo": self.__titulo,
            "autor": self.__autor,
            "genero": self.__genero,
            "anio_publicacion": self.__anio_publicacion,
            "cantidad_ejemplares": self.__cantidad_ejemplares
        }