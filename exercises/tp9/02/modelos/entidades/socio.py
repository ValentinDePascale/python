class Socios:

    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        if not isinstance(diccionario, dict):
            raise ValueError("Se esperaba diccioanrio instancia dict")
        if "dni" not in diccionario or "nombre" not in diccionario or "apellido" not in diccionario or "mail" not in diccionario or "anio_nacimiento" not in diccionario:
            raise Exception("El diccionario debe contener: 'dni', 'nombre', 'apellido', 'mail', 'anio_nacimiento'")
        return cls(
            dni = diccionario["dni"],
            nombre = diccionario["nombre"],
            apellido = diccionario["apellido"],
            mail = diccionario["mail"],
            anio_nacimiento = diccionario["anio_nacimiento"]

        )

    #Metodos de instancia
    def __init__(self, dni:int, nombre:str, apellido:str, mail:str, anio_nacimiento:int):
        if not isinstance(dni, int) or dni < 0:
            raise ValueError("El DNI debe ser entero positivo")
        
        if not isinstance(nombre,str) or nombre.strip() == "" or nombre.isspace():
            raise ValueError("El nombre debe ser texto valido")

        if not isinstance(apellido,str) or apellido.strip() == "" or apellido.isspace():
            raise ValueError("El apellido debe ser texto valido")
        
        if not isinstance(mail,str) or mail.strip() == "" or mail.isspace():
            raise ValueError("El mail debe ser texto valido")
        
        if not isinstance(anio_nacimiento, int) or anio_nacimiento < 0 or anio_nacimiento > 2025:
            raise ValueError("La fecha de nacimiento debe ser entero positivo")
        

        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__anio_nacimiento = anio_nacimiento
        

    #consultas
    def obtenerDni(self)->int:
        return self.__dni
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerApellido(self)->str:
        return self.__apellido
    
    def obtenerMail(self)->str:
        return self.__mail
    
    def obtenerAnioNacimiento(self)->int:
        return self.__anio_nacimiento
    
    #comandos
    def establecerDni(self, dni:int):
        if not isinstance(dni, int) or dni < 0:
            raise ValueError("El DNI debe ser entero positivo")
        self.__dni = dni

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre,str) or nombre.strip() == "" or nombre.isspace():
            raise ValueError("El nombre debe ser texto valido")
        self.__nombre = nombre

    def establecerApellido(self, apellido:str):
        if not isinstance(apellido,str) or apellido.strip() == "" or apellido.isspace():
            raise ValueError("El apellido debe ser texto valido")
        self.__apellido = apellido

    def establecerMail(self, mail:str):
        if not isinstance(mail,str) or mail.strip() == "" or mail.isspace():
            raise ValueError("El mail debe ser texto valido")
        self.__mail = mail

    def establecerAnioNacimiento(self, anio_nacimiento:int):
        if not isinstance(anio_nacimiento, int) or anio_nacimiento < 0 or anio_nacimiento > 2025:
            raise ValueError("La fecha de nacimiento debe ser entero positivo")
        self.__anio_nacimiento = anio_nacimiento


    def esIgual(self, otroSocio)->bool:
        if not isinstance(otroSocio, Socios):
            raise ValueError("El argumento debe ser un objeto de la clase Socio")
        return self.__dni == otroSocio.obtenerDni()

    def __str__(self):
        return (f"DNI: {self.__dni} /n"
                f"Nombre: {self.__nombre} /n"
                f"Apellido: {self.__apellido} /n"
                f"Mail: {self.__mail} /n"       
                f"Año de Nacimiento: {self.__anio_nacimiento} /n")
    
    def toDiccionario(self)->dict:
        return{
            "dni": self.__dni,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "mail": self.__mail,
            "anio_nacimiento": self.__anio_nacimiento
        }


        