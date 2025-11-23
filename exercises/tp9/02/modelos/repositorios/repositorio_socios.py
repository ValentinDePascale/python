from modelos.entidades.socio import Socios
import json

class RepositorioSocios:
    __RUTA_ARCHIVO = "datos\socios.json"

    def __init__(self):
        self.__socios = []
        self.__cargarDesdeArchivos()

    def __cargarDesdeArchivos(self):
        try:
            with open(self.__RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                datos_cargados = json.load(archivo)
                for socios in datos_cargados:
                    self.__socios.append(Socios.fromDiccionario(socios))
        except FileNotFoundError:
            print("El archivo de datos no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar los datos desde el archivo: {e}")


    def __guardarEnArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                datos_a_guardar = []
                for socios in self.__socios:
                    datos_a_guardar.append(socios.toDiccionario())
                json.dump(datos_a_guardar, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")



    def verificar_existe_socio(self, otroSocio)->bool:
        if not isinstance(otroSocio, Socios):
            raise ValueError("El socio buscado debe ser instancia de Socios")
        
        for s in self.__socios:
            if s == otroSocio:
                return True

        return False    


    #GET ALL

    def obtener_todos_socios(self)->list[Socios]:
        return self.__socios
    
    #GET INDIVIDUAL (DNI)

    def obtener_socio_dni(self, dni:int)-> Socios | None:
        if not isinstance(dni, int) or dni < 0:
            raise ValueError("El dni a buscar debe ser entero valido")
        
        for s in self.__socios:
            if s.obtenerDni() == dni:
                return s
        return None
    
    #POST AGREGAR SOCIO

    def agregar_nuevo_socio(self, nuevoSocio:Socios)->bool:
        if not isinstance(nuevoSocio, Socios):
            raise ValueError("El nuevo socio debe ser instancia de Socios")
        if not self.verificar_existe_socio(nuevoSocio):
            self.__socios.append(nuevoSocio)
            self.__guardarEnArchivo()
            return True    
        return False


    #PUT MODIFICAR (DNI)

    def modificar_un_socio(self, dni:int, dict_socio:dict)->bool:
        sociosAModificar = self.obtener_socio_dni(dni)
        if sociosAModificar:
            if "nombre" in dict_socio:
                sociosAModificar.establecerNombre(dict_socio["nombre"])
            if "apellido" in dict_socio:
                sociosAModificar.establecerApellido(dict_socio["apellido"])
            if "mail" in dict_socio:
                sociosAModificar.establecerMail(dict_socio["mail"])
            if "anio_nacimiento" in dict_socio:
                sociosAModificar.establecerAnioNacimiento(dict_socio["anio_nacimiento"])
            self.__guardarEnArchivo()
            return True
        return False
    

    #ELIMINAR SOCIO (DNI)
    def eliminar_socio(self, dni:int)->bool:
        if not isinstance(dni, int) or dni < 0:
            raise ValueError("El dni a buscar debe ser entero valido")
        
        socioAEliminar = self.obtener_socio_dni(dni)
        if socioAEliminar:
            self.__socios.remove(socioAEliminar)
            self.__guardarEnArchivo()
            return True
        return False