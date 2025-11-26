from modelos.entidades.alumno import Alumno
import json

class RepositorioAlumno:
    __RUTA_ARCHIVO = "datos/alumnos.json"

    def __init__(self):
        self.__alumnos = []
        self.__cargarDesdeArchivo()

    def __cargarDesdeArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                datos_cargados = json.load(archivo)
                if "ultimo_id" in datos_cargados:
                    ultimo_id = datos_cargados["ultimo_id"]
                    Alumno.establecerUltimoID(ultimo_id)
                if "alumnos" in datos_cargados:
                    lista_alumnos = datos_cargados["alumnos"]
                    for alumno_diccionario in lista_alumnos:
                        alumno = Alumno.fromDiccionario(alumno_diccionario)
                        self.__alumnos.append(alumno)
        except Exception as e:
            print(f"Error al cargar los datos desde el archivo: {e}")

    def __guardarEnArchivo(self):
        # primero generamos la lista de diccionarios de alumnos
        lista_alumnos_diccionarios = []
        for alumno in self.__alumnos:
            lista_alumnos_diccionarios.append(alumno.toDiccionario())
        # luego obtenemos el último ID utilizado por la clase
        ultimo_id_utilizado = Alumno.obtenerUltimoID()
        # preparamos el diccionario completo para guardar
        datos_a_guardar = {"ultimo_id": ultimo_id_utilizado, "alumnos": lista_alumnos_diccionarios}
        try:            
            with open(self.__RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                json.dump(datos_a_guardar, archivo, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")

    def existeLegajo(self, legajo:int)->bool:
        if not isinstance(legajo, int) or legajo <= 0:
            raise TypeError("El legajo debe ser un entero positivo.")
        
        for a in self.__alumnos:
            if a.obtenerLegajo() == legajo:
                return True
        return False

    def existeAlumno(self, otroAlumno:Alumno)->bool:
        if not isinstance(otroAlumno, Alumno):
            raise ValueError("El argumento debe ser una instancia de Alumno.")
        
        for a in self.__alumnos:
            if a == otroAlumno:
                return True
        return False

    #GET ALL
    def obtenerTodos(self)->list[Alumno]:
        return self.__alumnos
    
    #GET x LEGAJO
    def obtenerPorLegajo(self, legajo:int)-> Alumno | None:
        if self.existeLegajo(legajo):
            for a in self.__alumnos:
                if a.obtenerLegajo() == legajo:
                    return a
        else:
            return None

    #POST ALUMNO

    def agregarAlumno(self, nuevoAlumno:Alumno)->bool:
        if not isinstance(nuevoAlumno, Alumno):
            raise ValueError("El alumno debe ser instancia de Alumno")
    
        if not self.existeAlumno(nuevoAlumno):
            self.__alumnos.append(nuevoAlumno)
            self.__guardarEnArchivo()
            return True
        else:
            return False
        
    #PUT X LEGAJO

    def actualizarAlumno(self, legajo:int, datos_dict:dict)->bool:
        alumnoActualiar = self.obtenerPorLegajo(legajo)

        if alumnoActualiar is not None:
            if "nombre" in datos_dict:

                nuevo_nombre = datos_dict["nombre"]
                if isinstance(nuevo_nombre, str) and nuevo_nombre.strip() != "":
                    alumnoActualiar.establecerNombre(nuevo_nombre)
                else:
                    raise ValueError("Se esperaba nombre como texto")
                
            if "apellido" in datos_dict:
                nuevo_apellido = datos_dict["apellido"]

                if isinstance(nuevo_apellido, str) or nuevo_apellido.strip() != "":
                    alumnoActualiar.establecerApellido(nuevo_apellido)
                else:
                    raise ValueError("Se esperaba apellido como texto")
            self.__guardarEnArchivo()
            return True
        else:
            return False
        
    #ELIMINAR X LEGAJO

    def eliminarAlumno(self, legajo:int)->bool:
        alumnoEliminar = self.obtenerPorLegajo(legajo)

        if alumnoEliminar is not None:
            self.__alumnos.remove(alumnoEliminar)
            self.__guardarEnArchivo()
            return True
        else:
            return False