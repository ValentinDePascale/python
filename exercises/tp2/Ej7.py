FILE_PATH = r"C:\Users\nelic\OneDrive\Documentos\Valentin\Universidad\Programacion II\Python\Archivos\productos.txt"

lista = []
try:
    with open(FILE_PATH, "r") as archivo:
        for i in archivo:
            partes = i.strip().split(";")
            if len(partes) == 3:
                lista.append({
                    "codigo": partes[0],
                    "nombre": partes[1],
                    "precio": partes[2]
                })


except FileNotFoundError:
    print("Archivo no encontrado")


print (lista)