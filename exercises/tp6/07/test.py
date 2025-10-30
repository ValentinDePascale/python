from cuidadores import Cuidador
from mascota import Mascota

class Test:
    @staticmethod
    def run():
        m1 = Mascota("Loli", "Gato", 14, "Gata hermosa")
        m2 = Mascota("Omi", "Gato", 3, "Gato gris hermoso")
        m3 = Mascota("Tango", "Perro", 12, "Golden hermoso")

        c1 = Cuidador("Valen", "Alvear", 123123123)
        c2 = Cuidador("Mori", "Lucas abad", 1212334121)


        c1.asignarMascota(m1)
        c2.asignarMascota(m2)
        c2.asignarMascota(m3)

        print("Mascotas"+"-"*50)

        print(m1)
        print(m2)
        print(m3)


        print("Cuidadores"+"-"*50)
        print(c1)
        print(c2)


        c1.mostrarMascota()
        c2.mostrarMascota()




if __name__ == "__main__":
    Test.run()