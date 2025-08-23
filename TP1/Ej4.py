def ingresar_entero(mensaje):
    esValido = False
    while esValido == False:
        try:
            num = int(input(mensaje))
            if num > 0:
                esValido = True
            else:
                print("No se permiten numeros negativos.")
        except ValueError:
            print("Mal ingreso. Intentelo nuevamente")
    return num

lista = []

for i in range (3):
    num = ingresar_entero(f"Ingrese el {i+1}° numero: ")
    lista.append(num)


lista.sort()

print(f"El mayor numero es: {lista[-1]}")



