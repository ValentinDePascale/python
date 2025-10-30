from libro import Libro
import json
from pathlib import Path


class Test:
    @staticmethod
    def run():
        libros_desde_json = []
        base = Path(__file__).resolve().parent
        ruta = base / "libros.json"
        
        with ruta.open ("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        for linea in datos:
            libro = Libro.form_diccionario(json.dumps(linea, ensure_ascii=False))
            libros_desde_json.append(libro)


        ingresoAnio = int(input("El ingrese el año de publicacion: "))


        for l in libros_desde_json:
            if ingresoAnio == l.obtenerAnioPublicacion():
                print(l)


if __name__ == "__main__":
    Test.run()