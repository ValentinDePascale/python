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

def cargarNotas()->int:
    esValido = False
    while not esValido:
        try:
            nota = int(input())
            if nota >= 0 and nota <= 100:
                esValido = True
            else: 
                print("Mal ingreso. Por favor, ingrese un entero positivo")
        except ValueError:
                print("Mal ingreso. Por favor, ingrese un entero positivo")
    return nota

def notaAlta(notas:list):
    masalta = max(notas)
    return masalta


cantnotas = verificar_entero("Cuantas notas desea cargar?: ")
notas = []
for i in range (cantnotas):
    print(f"Ingrese la {i+1}° nota: ", end=" ")
    notas.append(cargarNotas())


notaAlta = notaAlta(notas)
print(f"La nota más alta es: {notaAlta} su indice es {notas.index(notaAlta)}")
    