FILE_PATH = r"C:\Users\nelic\OneDrive\Documentos\Valentin\Universidad\Programacion II\Python\Archivos\datos.txt"

try:
    with open(FILE_PATH, "r") as archivo:
        lista_archivo = [int(i.strip()) for i in archivo if i.strip() != ""]

except FileNotFoundError:
    print("El archivo no fue encotrado")

print (lista_archivo)