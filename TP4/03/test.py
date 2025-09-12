from vinoteca import Vinoteca

class test:
    @staticmethod
    def ejectuar():
        try:
            vinoteca = Vinoteca()
            print(20*"-"+" VINOTECA "+"-"*20)
            print(f"Jugos {vinoteca.obtenerCantidadJugos()}")
            print(f"Blanco {vinoteca.obtenerCantidadVinosBlancos()}")
            print(f"Tinto Joven {vinoteca.obtenerCantidadVinosTintosJovenes()}")
            print(f"Tinto Anejado {vinoteca.obtenerCantidadVinosTintosAnejados()}")

            vinoteca.venderJugos(500)
            vinoteca.venderVinosBlanco(700)
            vinoteca.venderVinosTintosJovenes(5000)
            vinoteca.venderVinosTintosAnejados(6000)

            print(20*"-"+" VINOTECA "+"-"*20)
            print(f"Jugos {vinoteca.obtenerCantidadJugos()}")
            print(f"Blanco {vinoteca.obtenerCantidadVinosBlancos()}")
            print(f"Tinto Joven {vinoteca.obtenerCantidadVinosTintosJovenes()}")
            print(f"Tinto Anejado {vinoteca.obtenerCantidadVinosTintosAnejados()}")

            vinoteca.reponerJugos()
            vinoteca.reponerVinosBlancos()
            vinoteca.reponerVinoTintoJoven()
            vinoteca.reponerVinoTintoAnejado()

            
            print(20*"-"+" VINOTECA "+"-"*20)
            print(f"Jugos {vinoteca.obtenerCantidadJugos()}")
            print(f"Blanco {vinoteca.obtenerCantidadVinosBlancos()}")
            print(f"Tinto Joven {vinoteca.obtenerCantidadVinosTintosJovenes()}")
            print(f"Tinto Anejado {vinoteca.obtenerCantidadVinosTintosAnejados()}")

        except ValueError as error:
            print(f"Error. {error}")
        except TypeError as error:
            print(f"Error. {error}")

if __name__ == "__main__":
    test.ejectuar()