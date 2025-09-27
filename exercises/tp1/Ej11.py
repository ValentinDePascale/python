def verificarEntero(mensaje:str)->int:
    esValido = False
    while not esValido:
        try:
            numero = int(input(mensaje))
            esValido = True
        except ValueError:
            print("Mal ingreso. Ingrese un numero entero positivo")
    return numero

num = 0
cont = 0
suma = 0
print("Ingrese numeros enteros positivos, finalice con uno negativo: ")

while num >= 0:
    num = verificarEntero("Ingrese un numero: ");
    if num >= 0:
        cont += 1
        suma += num

promedio=suma/cont
print(f"El promedio es {promedio} con un total de {cont} ingresos.")
