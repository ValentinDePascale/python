from modelos.entidades.examenasignado import ExamenAsignado
import json

class RepositorioExamenesAsignados:
    __RUTA_ARCHIVO = "datos/examenes_asignados.json"

    def __init__(self):
        self.__examenes_asignados = []
        self.__cargarDesdeArchivo()

    def __cargarDesdeArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                for examen_dict in datos:
                    examen = ExamenAsignado.fromDiccionario(examen_dict)
                    self.__examenes_asignados.append(examen)
        except Exception:
            print("No se pudo cargar el archivo de examenes asignados. Se iniciará con una lista vacía.")
    
    def __guardarEnArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding='utf-8') as archivo:
                datos = []
                for examen in self.__examenes_asignados:
                    datos.append(examen.toDiccionario())
                json.dump(datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"No se pudo guardar el archivo de examenes asignados: {e}")

    #metodo para el GET de todos los examenes asignados
    def obtenerTodos(self):
        return self.__examenes_asignados
    
    #metodo para el GET de examenes asignados por legajo
    def obtenerPorLegajo(self, legajo:int):
        for examen in self.__examenes_asignados:
            if examen.obtenerLegajo() == legajo:
                return examen
        return None
    
    #metodo para el POST de examenes asignados
    def agregarExamenAsignado(self, examen:ExamenAsignado)->bool:
        if not isinstance(examen, ExamenAsignado):
            raise ValueError("El examen asignado debe ser una instancia de ExamenAsignado.")
        if not self.existeExamenAsignado(examen.obtenerLegajo()):
            self.__examenes_asignados.append(examen)
            self.__guardarEnArchivo()
            return True
        return False

    def existeExamenAsignado(self, legajo:int):
        for examen in self.__examenes_asignados:
            if examen.obtenerLegajo() == legajo :
                return True
        return False
    
    #metodo para el PUT de examenes asignados
    def actualizarExamenAsignado(self, legajo:int, dictDatos:dict):
        examen = self.obtenerPorLegajo(legajo)
        if examen is not None:
            if "numeroTema" in dictDatos:
                examen.establecerNumeroTema(dictDatos["numeroTema"])
            if "confirmado" in dictDatos:
                examen.establecerConfirmado(dictDatos["confirmado"])
            self.__guardarEnArchivo()
            return True
        return False
    
    #metodo para el DELETE de examenes asignados
    def eliminarExamenAsignado(self, legajo:int):
        for examen in self.__examenes_asignados:
            if examen.obtenerLegajo() == legajo:
                self.__examenes_asignados.remove(examen)
                self.__guardarEnArchivo()
                return True
        return False