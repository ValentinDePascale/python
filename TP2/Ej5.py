alumnos = {
    "nombre": [],  
    "nota": [],
    "estado": []
}

def verificar_entero(mensaje:str)->int:
    esValido = False
    while not esValido:
        try:
            entero = int(input(mensaje))
            if entero > 0:
                esValido = True
            else: 
                print("Mal ingreso. Por favor, ingrese un entero positivo")
        except ValueError:
            print(f"Mal ingreso. {mensaje}")
    return entero

def cargarAlumnos(posicion):
    alumnos["nombre"].append (input(f"Ingrese el nombre del alumno {posicion+1}:  "))
    alumnos["nota"].append(verificar_entero(f"Ingrese nota del alumno {posicion+1}: "))
    if alumnos["nota"][posicion] >= 40:
        alumnos["estado"].append("Aprobado")
    else:
        alumnos["estado"].append("Desaprobado")



cantidaAlumnos = verificar_entero("Ingrese cantidad de alumnos: ")
for i in range (cantidaAlumnos):
    cargarAlumnos(i)
   
for i in range (cantidaAlumnos):
    print(f"NOMBRE: {alumnos["nombre"][i]}", end=" ")
    print(f"NOTA: {alumnos["nota"][i]}", end=" ")
    print(f"ESTADO: {alumnos["estado"][i]}")



