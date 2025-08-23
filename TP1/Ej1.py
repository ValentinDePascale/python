def leer_float(mensaje):
    esValido = False
    while esValido == False:
        try:
            numero = float(input(mensaje))
            if numero > 1:
                esValido = True
            else:
                print("El numero debe ser mayor a 0")
        except ValueError:
            print("Mal Ingreso. Intentar nuevamente")
    return numero

def tipo_de_triangulo():
    if lado1 == lado2 == lado3:
        print("Sus tres lados son iguales, el triangulo es Equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Sus dos de sus tres lados son iguales, el triangulo es Isósceles")
    else:
        print("Sus tres lados son distintos, el triangulo es Escaleno")





lado1 = leer_float("Ingrese primero lado: ")
lado2 = leer_float("Ingrese segundo lado: ")
lado3 = leer_float("Ingrese tercer lado: ")

tipo_de_triangulo()




