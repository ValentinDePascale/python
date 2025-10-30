class Disciplina:
    def __init__(self, nombre:str, descripcion:str):
        if not isinstance(nombre, str) or nombre.strip() == "" or nombre.isspace():
            raise ValueError("Error. El nombre debe ser un string valido")
        if not isinstance(descripcion, str) or descripcion.strip() == "" or descripcion.isspace():
            raise ValueError("Error. La descripcion debe ser un string valido")
        

        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__participantes = []
    
    def obtenerNombreDisciplina(self)->str:
        return self.__nombre

    def obtenerDescripcion(self)->str:
        return self.__descripcion
    
    def obtenerParticipantes(self):
        for participante in self.__participantes:
            return(f"{participante.obtenerNombre()}, {participante.obtenerNacionalidad()}, {participante.obtenerEdad()}") 
    
    def agregarParticipante(self, participante:"Participante"):
        if participante not in self.__participantes:
            self.__participantes.append(participante)
    
    def __str__(self):
        return (f"DISCIPLINA \n"
                f"Nombre: {self.obtenerNombreDisciplina()} \n"
                f"Descripcion: {self.obtenerDescripcion()} \n"
                f"Participantes: {self.obtenerParticipantes()}"
        )