def verificarEntero(mensaje:str)->int:
    esValido = False
    while not esValido:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                   if numero < 40: 
                    esValido = True
                   else:
                       print("Ingrese un numero menor a 40")
            else: 
                print("Por favor, ingrese un numero positivo")
        except ValueError: 
            print("Mal ingreso. Ingrese un numero entero positivo")
    return numero

def imprimirCuadrado (alto, ancho):
    print("*"*ancho)
    for i in range (alto-2):
        print ("*"+" "*(ancho-2)+"*")
    print("*"*ancho)



alto = verificarEntero("Ingrese alto: ")
ancho = verificarEntero("Ingrese ancho: ")

imprimirCuadrado(alto, ancho)




