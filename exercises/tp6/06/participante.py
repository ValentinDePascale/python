from disciplina import Disciplina

class Participante:
    def __init__(self, nombre:str, edad:int, nacionalidad:str):
        if not isinstance(nombre, str) or nombre.strip() == ""  or nombre.isspace():
            raise ValueError("El nombre debe ser string valido")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edada debe ser entera positiva")
        if not isinstance(nacionalidad, str) or nacionalidad.strip() == ""  or nacionalidad.isspace():
            raise ValueError("El nombre debe ser string valido")

        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplina = []

    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEdad(self)->int:
        return self.__edad
    
    def obtenerNacionalidad(self)->str:
        return self.__nacionalidad
    
    def obtenerDisciplinas(self)->"Disciplina":
        for disci in self.__disciplina:
            return disci.obtenerNombreDisciplina()

    def establecerDisciplina(self, disci:"Disciplina"):
        if not isinstance(disci, Disciplina):
            return TypeError("Error. La disciplina debe ser instancia de Disciplina")
        if disci not in self.__disciplina:
            self.__disciplina.append(disci)
            disci.agregarParticipante(self)

    def __str__(self):


        return (f"PARTICIPANTE \n"
                f"Nombre: {self.obtenerNombre()} \n"
                f"Edad: {self.obtenerEdad()} \n"
                f"Nacionalidad: {self.obtenerNacionalidad()} \n"
                f"Disciplina/s: {self.obtenerDisciplinas()}"
        )