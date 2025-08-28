def ingreso_entero(mensaje):
    esValido = False
    while esValido == False:
        try:
            num = int(input(mensaje))
            if num > 0:
                esValido = True
            else:
                print("Por favor, ingrese un numero entero positivo")
        except ValueError:
                print("Mal ingreso. Intentelo nuevamente")        
    return num
        

num_solicitado = ingreso_entero("Ingrese un numero entero: ")

for i in range (1, num_solicitado+1):
    print(f"{i} ", end=" ")
    