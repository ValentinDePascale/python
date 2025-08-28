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

def comprobarUnCaracter(mensaje:str)->str:
    unCatacter = False
    while not unCatacter:
        caracter = input(mensaje)
        if len(caracter) == 1:
            unCatacter = True
        else:
            print(f"Mal ingreso. Por favor, {mensaje}")
    return caracter

car = comprobarUnCaracter("Ingrese un caracter: ")
num = verificarEntero("Ingrese la cantidad de repeticiones: ")

print(car*num)