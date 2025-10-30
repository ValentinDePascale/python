from polizainmueble import PolizaInmueble
from polizainmuebleescolar import PolizaInmuebleEscolar
from aseguradora import Aseguradora 
class Test:
    @staticmethod
    def run():
        poliza1 = PolizaInmueble(1, 500, 250.12, 125.5)
        poliza2 = PolizaInmueble(2, 400, 170.20, 245.2)

        polizaescolar1 = PolizaInmuebleEscolar(3, 1000, 321.1, 354, 20, 250.3, 300, 10.4)
        polizaescolar2 = PolizaInmuebleEscolar(4, 1200, 211.4, 541.1, 15, 170, 200, 11)
        aseguradora1 = Aseguradora()
        aseguradora2 = Aseguradora()

        print(poliza1)
        print(poliza2)

        print(polizaescolar1)
        print(polizaescolar2)


        print(f"Costo poliza1:{poliza1.costoPoliza()}")
        print(f"Costo poliza1:{poliza2.costoPoliza()}")
        print(f"Costo poliza1:{polizaescolar1.costoPoliza()}")
        print(f"Costo poliza1:{polizaescolar2}.costoPoliza()}")


        aseguradora1.insertar(poliza2)
        aseguradora1.insertar(poliza1)

        aseguradora2.insertar(poliza1)
        aseguradora2.insertar(poliza2)

        aseguradora1.eliminar(poliza1)

        if aseguradora1.existePoliza(poliza2):
            print("existe la poliza 2 en la aseguradora 1")
        
        if aseguradora2.hayPolizas():
            print ("Hay polizas en asegu 2")

        if aseguradora1.esIgual(aseguradora2):
            print("aseguradora 1 es igual a 2")
        else:
            print("no son iguales")



if __name__ == "__main__":
    Test.run()