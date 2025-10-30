import json
class Libro:
    def __init__(self, titulo:str, autor:str, genero:str, anioPublicacion:int, ISBN:str):
        if not isinstance(titulo, str) or titulo.strip() == "" or titulo.isspace():
            raise ValueError("El titulo debe ser string valido")
        if not isinstance(autor, str) or autor.strip() == "" or autor.isspace():
            raise ValueError("El autor debe ser string valido")
        if not isinstance(genero, str) or genero.strip() == "" or genero.isspace():
            raise ValueError("El genero debe ser string valido")
        if not isinstance(anioPublicacion, int) or anioPublicacion < 0 or anioPublicacion > 2025:
            raise ValueError("El titulo debe ser entero valido")
        if not isinstance(ISBN, str) or ISBN.strip() == "" or ISBN.isspace():
            raise ValueError("El ISBN debe ser string valido")
        
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anioPublicacion = anioPublicacion
        self.__ISBN = ISBN


    def obtenerAnioPublicacion(self)->int:
        return self.__anioPublicacion

    def to_diccionario(self):
        dicc_libro = {"titulo": self.__titulo, "autor": self.__autor, "genero": self.__genero, "anioPublicacion": self.__anioPublicacion, "ISBN": self.__ISBN}
        return json.dump(dicc_libro, ensure_ascii=False)
    
    @classmethod
    def form_diccionario(cls, json_data):
        datos = json.loads(json_data)
        return cls(datos["titulo"], datos["autor"], datos["genero"], datos["anioPublicacion"], datos["ISBN"])
    

    def __str__(self):
      return f"{self.__titulo} - {self.__autor} ({self.__anioPublicacion})"