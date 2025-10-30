from evento import Evento
class Organizador:
    def __init__(self, nombre:str, email:str, especialidad:str):
        if not isinstance(nombre, str) or nombre.strip() == ""  or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(email, str) or email.strip() == ""  or email.isspace():
            raise ValueError("El email debe ser string valido")
        if not isinstance(especialidad, str) or especialidad.strip() == ""  or email.isspace():
            raise ValueError("La especialidad debe ser string valido ")

        self.__nombre = nombre
        self.__email = email
        self.__especialidad = especialidad
        self.__eventos_organizados = []

    
    def asignarEvento(self, evento:"Evento"):
        if isinstance(evento, Evento):
            self.__eventos_organizados.append(evento)
        else:
            raise TypeError("El evento debe ser instancia de Evento")

    def __str__(self):
        return (f"Nombre: {self.__nombre}, Email: {self.__email}, Especialidad: {self.__especialidad}")

