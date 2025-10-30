class Participante:
    def __init__(self, nombre:str, email:str, telefono:str):
        if not isinstance(nombre, str) or nombre.strip() == ""  or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(email, str) or email.strip() == ""  or email.isspace():
            raise ValueError(" El emaildebe ser string valido")
        if not isinstance(telefono, str) or telefono.strip() == ""  or telefono.isspace():
            raise ValueError("El telefono debe ser entera positiva")


        self.__nombre = nombre
        self.__email = email
        self.__telfono = telefono

    def __str__(self):
        return (f"Nombre: {self.__nombre}, Email: {self.__email}, Telefono: {self.__telfono}")