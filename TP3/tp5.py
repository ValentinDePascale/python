def validarNum(mensaje:str)->int:
    esValido = False
    while not esValido:
        try:
            num = int(input(mensaje))
            if num >= 0:
                esValido = True
            else:
                print("Error.")
        except ValueError: 
            print(f"Error. {mensaje}") 
    return num

def primo (num:int)->bool:
    esPrimo = True

    if num < 2:
        esPrimo = False
    for i in range (2, num):
        if num % i == 0:
            esPrimo = False
    return esPrimo


inicio = validarNum("Ingrese 1° numero: ")
final = validarNum("Ingrese 2° numero: ")

lista_primos = [i for i in range (inicio, final) if primo(i)]

print(lista_primos)