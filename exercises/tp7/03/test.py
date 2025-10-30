from departamento import Departamento
from inmobiliaria import Inmobiliaria
from inmueble import Inmueble
from propieterio import Propietario
from quinta import Quinta

class Test:
  @staticmethod
  def ejecutar():
     
    p1 = Propietario("Valen", 54234543)
    p2 = Propietario("Mo", 918231234)

    
    inmueble1 = Inmueble(1, "Alvear", 20, 10)
    inmueble2 = Inmueble(2, "11 de Abril", 15, 7)

    inmueble1.establecerPropietario (p1)
    inmueble2.establecerPropietario(p2)

if __name__ == "__main__":
    Test.ejecutar() 