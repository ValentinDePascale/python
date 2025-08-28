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

cantNumeros = ingreso_entero("Ingrese la cantidad de numeros que quiera ingresar: ")
suma = 0
for i in range (cantNumeros):
    num = ingreso_entero(f"Ingrese el {i+1}° numero: ")
    suma += num

promedio = suma / cantNumeros
print(f"El promedio de los {cantNumeros} ingresados es: {promedio}")
