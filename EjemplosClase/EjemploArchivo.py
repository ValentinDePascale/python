ruta = r"C:\Users\nelic\OneDrive\Documentos\Valentin\Universidad\Programacion II\Python\Archivos\texto.txt"
archivo = open(ruta, "r")
cont = 0

for i in archivo:
    cont += 1

print(f"Cantidad de Lineas: {cont}")
archivo.close
