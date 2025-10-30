from inmueble import Inmueble
class Inmobiliaria:
    def __init__(self):

        self.__propiedades = []


    def insertarPropiedades(self, inmueble:"Inmueble"):
        if not isinstance(inmueble, Inmueble):
            raise TypeError("Error. El inmueble debe ser instancia de Inmueble")
        

    def insertar(self, inmueble:"Inmueble"):
        if not isinstance(inmueble, Inmueble):
            raise TypeError("Error. El inmueble debe ser instancia de Inmueble")
        
        if inmueble not in self.__propiedades:
            self.__propiedades.append(inmueble)
            print("Agregando inmueble")
        else:
            print("El inmueble ya existe en el seguro")

    def eliminar(self, inmueble:"Inmueble"):
        if not isinstance(inmueble, Inmueble):
            raise TypeError("Error. El inmueble debe ser instancia de Inmueble")
        
        if inmueble in self.__propiedades:
            self.__propiedades.remove(inmueble)
            print("Eliminando inmueble")

        else:
            print("El inmueble no esta en la propiedadad, no se puede borrar")


    def estaInmuebleCodigo(self, codigo:int)->bool:
        if not isinstance(codigo, int) or codigo < 0:
            raise TypeError("El codigo debe ser entero positivo")
        for inmu in self.__propiedades:
            if inmu.obtenerCodigo() == codigo:
                return True
        return False


    def estaInmueble(self, inmueble:"Inmueble")->bool:
        if not isinstance(inmueble, Inmueble):
            raise TypeError("Error. El inmueble debe ser instancia de Inmueble")
        for inmu in self.__propiedades:
            if inmu == inmueble:
                return True
        return False

    def esIgual(self, inmueble:"Inmueble")->bool:
        if not isinstance(inmueble, Inmueble):
            raise TypeError("Error. El inmueble debe ser instancia de Inmueble")
        return self == inmueble
           
    def hayInmuebles(self)->bool:
        if self.__propiedades:
            return True
        else:
            return False
        
    def contarPropiedadesMasMetros(self, metros:int)->int:
        if not isinstance(metros, int) or metros < 0:
            raise TypeError("El codigo debe ser entero positivo")
        return len(self.__propiedades) - metros

    def mayorPrecioVenta(self)->"Inmueble":
        mayorPrecio = 0
        inmuebleMasCaro = -1
        for inmu in self.__propiedades:
            if inmu.precioVenta() > mayorPrecio:
                inmuebleMasCaro = inmu
                mayorPrecio = inmu.precioVenta()

        return inmuebleMasCaro

        