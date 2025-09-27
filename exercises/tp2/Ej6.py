FILE_PATH = r"C:\Users\nelic\OneDrive\Documentos\Valentin\Universidad\Programacion II\Python\Archivos\distancias.txt"
suma = 0
promedio = 0

with open (FILE_PATH, "r") as file:
    contenido = file.readlines()
    for i in contenido:
        suma += int(i.strip())
    
    promedio = suma / len(contenido)
    
    print(f"Promedio: {promedio}", end=" ")

    for i in contenido:
        if int(i.strip()) >= promedio:
            print(i, end=",")

