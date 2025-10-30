from borde import Borde
from color import Color

class Test:
    @staticmethod
    def run():
        C1 = Color(150, 150, 150)
        C2 = Color(150, 150, 150)
        B1 = Borde(1,C1)
        B2 = Borde(1,C2)
        B3 = B2.clonar()
        B4 = Borde(B2.obtenerBorde(), B2.obtenerColor())
        print( B2 == B3)
        print( B2 == B4)
        print(B2.esIgualQue(B1))
        print(B2.esIgualQue(B3))
        print(B2.obtenerBorde() == B1.obtenerBorde() and
        B2.obtenerColor() == B1.obtenerColor())
        print(B2.obtenerBorde() == B3.obtenerBorde() and
        B2.obtenerColor() == B3.obtenerColor())
        print(B2.obtenerBorde() == B1.obtenerBorde() and
        B2.obtenerColor().esIgualQue(B1.obtenerColor()))
        print(B2.obtenerBorde() == B4.obtenerBorde() and
        B2.obtenerColor().esIgualQue(B4.obtenerColor()))


if __name__ == "__main__":
    Test.run()