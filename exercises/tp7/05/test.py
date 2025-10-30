from personal import Personal
from administrativo import Administrativo
from personal_mantenimiento import Mantenimiento
from programador import Programador


class Test:
    @staticmethod
    class run():
        A1 = Administrativo("Valentin", "De Pascale", 46626434, 22314, "Jefe")
        P1 = Programador("Juan", "Perez", 3214123, 43244, "E-Commerce")
        M1 = Mantenimiento("Emilio", "Gonzalez", 4324234, 4423, "Sistemas")


        print(A1.obtenerNombre())

        print(P1)

        print(M1.obtenerArea())

        