def verificarEntero(mensaje:str)->int:
    esValido = False
    while not esValido:
        try:
            numero = int(input(mensaje))
            if numero >= 0:
                esValido = True
        except ValueError:
            print("Mal ingreso. Ingrese un numero entero positivo")
    return numero

def verificarOrden (listaIngresados:list)->bool:
    listaOrdenda = listaIngresados.copy()
    listaOrdenda.sort()
    
    return listaIngresados == listaOrdenda


num = 1
listaIngresados = []
print("Ingrese numeros enteros, finalice con 0")
while num != 0:
    num = verificarEntero("Ingrese un numero: ")
    if num != 0:
        listaIngresados.append(num)

orden = verificarOrden(listaIngresados)

if orden:
    print("Estan ordenados")
else:
    print("No estan ordenados")
