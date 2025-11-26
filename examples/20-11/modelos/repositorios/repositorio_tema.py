from modelos.entidades.tema import Tema
import json

class RepositorioTema():
    __RUTA_ARCHIVO = "datos/temas.json"

    def __init__(self):
        self.__temas = []
        self.__cargarDesdeArchivo()

    def __cargarDesdeArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                for tema_dict in datos:
                    tema = Tema.fromDiccionario(tema_dict)
                    self.__temas.append(tema)
        except Exception:
            print("No se pudo cargar el archivo de temas. Se iniciará con una lista vacía.")
    
    def __guardarEnArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding='utf-8') as archivo:
                datos = []
                for tema in self.__temas:
                    datos.append(tema.toDiccionario())
                json.dump(datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"No se pudo guardar el archivo de temas: {e}")



    def existeTema(self, otroTema:Tema) -> bool:
        if not isinstance(otroTema, Tema):
            raise ValueError("El argumento debe ser una instancia de Tema.")
        
        for t in self.__temas:
            if t == otroTema:
                return True
        return False
    
    def existeNumero(self, numero:int) -> bool:
        if not isinstance(numero, int) or numero <= 0:
            raise TypeError("El número debe ser un entero positivo.")
        
        for t in self.__temas:
            if t.obtenerNumero() == numero:
                return True
        return False

    #GET ALL
    def obtenerTodos(self) -> list[Tema]:
        return self.__temas
    
    #GET POR NUMERO
    def obtenerPorNumero(self, numero:int) -> Tema | None:
        self.existeNumero(numero)

        for t in self.__temas:
            if t.obtenerNumero() == numero:
                return t
        return None
    
    #POST AGREGAR POR NUMERO
    def agregarTema(self, nuevoTema:Tema)->bool:
        if not self.existeTema(nuevoTema):
            self.__temas.append(nuevoTema)
            self.__guardarEnArchivo()
            return True
        else:
            return False
        
    #PUT MODIFICAR X NUMERO
    def modificarPorNumero(self, numero:int, datos_dict:dict)->bool:
        temaActualizar = self.obtenerPorNumero(numero)

        if temaActualizar is not None:
            if "nombre" in datos_dict:
                nombre_nuevo = datos_dict["nombre"]
                if isinstance(nombre_nuevo, str) and nombre_nuevo.strip() != "":
                    temaActualizar.establecerNombre(nombre_nuevo)
                else:
                    raise ValueError("El nuevo nombre debe ser una cadena de texto no vacía.")
            if "enunciado" in datos_dict:
                nuevo_enunciado = datos_dict["enunciado"]
                if isinstance(nuevo_enunciado, str) and nuevo_enunciado.strip() != "":
                    temaActualizar.establecerEnunciado(nuevo_enunciado)
                else:
                    raise ValueError("El nuevo enunciado debe ser una cadena de texto no vacía.")
            self.__guardarEnArchivo()
            return True
        else:
            return False


    #DELETE X NUMERO
    def eliminarPorNumero(self, numero:int)->bool:

        temaEliminar = self.obtenerPorNumero(numero)

        if temaEliminar is not None:
            self.__temas.remove(temaEliminar)
            self.__guardarEnArchivo()
            return True
        else:
            return False
                    

