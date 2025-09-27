def ingreso_entero(mensaje):
    esValido = False
    while not esValido:
        try:
            num = int(input(mensaje))
            if num > 0:
                esValido = True
            else:
                print("Por favor, ingrese un numero entero positivo")
        except ValueError:
            print("Mal ingreso. Intentelo nuevamente: ")
    return num

numero = ingreso_entero("Ingrese un numero entero positivo: ")

for i in range (1, numero+1):
    if i % 2 == 0:
        print(f"{i}", end=" ")