from modelos.entidades.polizainmueble import PolizaInmueble
from modelos.entidades.polizainmuebleescolar import PolizaInmuebleEscolar
import json

class RepositorioPolizas:
    __RUTA_ARCHIVO = "datos/polizas.json"

    def __init__(self):
        self.__polizas = []
        self.__cargarTodas()

    def __cargarTodas(self):
        try:
            with open(self.__RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                datos_cargados = json.load(archivo)
                for polizas in datos_cargados:
                    if polizas.get("cant_personas") is not None:
                        self.__polizas.append(PolizaInmuebleEscolar.fromDiccionario(polizas))
                    else:  
                        self.__polizas.append(PolizaInmueble.fromDiccionario(polizas))
        except FileNotFoundError:
            print("El archivo de datos no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar los datos desde el archivo: {e}")


    def __guardarTodas(self):
        try:
            with open(self.__RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                datos_a_guardar = []
                for p in self.__polizas:
                    datos_a_guardar.append(p.toDiccionario())
                json.dump(datos_a_guardar, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")

    #True si la Poliza existe (se le pasa atributo de clase)
    def existe(self, otraPoliza:PolizaInmueble | PolizaInmuebleEscolar)-> bool:
        if not isinstance (otraPoliza, (PolizaInmueble, PolizaInmuebleEscolar)):
            raise ValueError("La poliza debe ser instancia de Poliza Inmueble o Poliza Inmueble Escolar")
        
        for p in self.__polizas:    
            if otraPoliza == p:
                return True
        return False
    
    #True si la Poliza existe (se le pasa numero)
    def existeNumero(self, numero:int)-> bool:
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("El numero debe ser entero positivo")

        for p in self.__polizas:
            if p.obtenerNumero() == numero:
                return True
            
        return False
    
    def ingresosMensuales(self)->float:
        suma = 0
        for p in self.__polizas:
            suma = suma + p.valorMensualPoliza()
        
        return suma

    # ---------------------------- CRUD -----------------------------------------
    #GET ALL
    def obtenerTodas(self) -> list[PolizaInmueble | PolizaInmuebleEscolar]:
        return self.__polizas
    
    #GET POR NUMERO (INDIVIDUAL)
    def obtenerPorNumero(self, numero:int)-> PolizaInmueble | PolizaInmuebleEscolar | None:
        if self.existeNumero(numero):
            for p in self.__polizas:
                if p.obtenerNumero() == numero:
                    return p
        else:
            return None
        
    #POST AGREGAR
    def agregar(self, nuevaPoliza:PolizaInmueble | PolizaInmuebleEscolar)->bool:
        if not isinstance(nuevaPoliza, (PolizaInmueble, PolizaInmuebleEscolar)):
            raise ValueError("La poliza a agregar debe ser instancia de Poliza Inmueble o Poliza Inmueble Escolar")
        
        if not self.existe(nuevaPoliza):
            self.__polizas.append(nuevaPoliza)
            self.__guardarTodas()
            return True
        else:
            return False
        
    #PUT MODIFICAR POR NUMERO
    def modificarPorNumero(self, numero:int, polizaActualizada:PolizaInmueble | PolizaInmuebleEscolar)->bool:
        if not isinstance(polizaActualizada, (PolizaInmueble, PolizaInmuebleEscolar)):
            raise ValueError("La poliza a agregar debe ser instancia de Poliza Inmueble o Poliza Inmueble Escolar")
        
        if self.existeNumero(numero):
            polizaAModificar = self.obtenerPorNumero(numero)
            if isinstance (polizaAModificar, PolizaInmuebleEscolar):
                if not isinstance(polizaActualizada, PolizaInmuebleEscolar):
                    raise TypeError("Se intenta actualizar una Póliza Escolar con un objeto de Póliza Inmueble base.")
                
                polizaAModificar.establecerIncendio(polizaActualizada.obtenerIncendio())
                polizaAModificar.establecerExplosion(polizaActualizada.obtenerExplosion())
                polizaAModificar.establecerRobo(polizaActualizada.obtenerRobo())
                polizaAModificar.establecerCantPersonas(polizaActualizada.obtenerCantPersonas())
                polizaAModificar.establecerMontoEquipamiento(polizaActualizada.obtenerMontoEquipamiento())
                polizaAModificar.establecerMontoMobiliario(polizaActualizada.obtenerMontoMobiliario())
                polizaAModificar.establecerMontoPersona(polizaActualizada.obtenerMontoPersona())
                self.__guardarTodas()
                return True
            else:
                polizaAModificar.establecerIncendio(polizaActualizada.obtenerIncendio())
                polizaAModificar.establecerExplosion(polizaActualizada.obtenerExplosion())
                polizaAModificar.establecerRobo(polizaActualizada.obtenerRobo())
                self.__guardarTodas()
                return True
        else:
            return False
        
    #DELETE ELIMINAR POR NUMERO
    def eliminarPorNumero(self, numero:int)->bool:
        if self.existeNumero(numero):
            polizaAEliminar = self.obtenerPorNumero(numero)
            self.__polizas.remove(polizaAEliminar)
            self.__guardarTodas()
            return True
        
        return False


