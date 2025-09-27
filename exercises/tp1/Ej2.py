def leer_float(mensaje):
    esValido = False
    while esValido == False:
        try:
            num = float(input(mensaje))
            if num > 0:
                esValido = True
            else:
                print("Ingrese un numero positivo")
        except ValueError:
          print("Mal ingreso")

alto = leer_float("Ingrese el alto: ")
ancho = leer_float("Ingrese el ancho: ")
largo = leer_float("Ingrese el largo: ")
