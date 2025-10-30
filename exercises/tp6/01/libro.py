class Libro:
    def __init(self, nombre:str, autor:str, editorial:str, categoria:str):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
                raise ValueError("Error")
        if not isinstance(autor, str) or autor == "" or autor.isspace():
                raise ValueError("Error")
        if not isinstance(editorial, str) or editorial == "" or editorial.isspace():
                raise ValueError("Error")
        if not isinstance(categoria, str) or categoria == "" or categoria.isspace():
                raise ValueError("Error")

        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria

    #CONSULTAS
    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerAutor(self)->str:
        return self.__autor
    def obtenerEditorial(self)->str:
        return self.__editorial
    def obtenerCategoria(self)->str:
        return self.__categoria