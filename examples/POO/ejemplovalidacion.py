def pedirNumeroPositivo()->int:
    num = int(input("Ingrese numero positivo: "))

def pedirTexto()->str:
    txt = input("Ingrese texto: ")

def validarNumero(numero:int)->bool:
    if not isinstance(numero, int):
        raise TypeError("Error de tipeo")
    if numero <= 0:
        raise ValueError("Error de valor")
    return True
    

def validarTexto(texto:str)->bool:
    if not isinstance(texto, str):
        raise TypeError("No es texto")
    if texto == "" or texto.isspace():
        raise ValueError("El texto esta vacio")
    if texto.isalnum():
        raise TypeError("Es un numero")
    return True

def main():
    try:
        numero = pedirNumeroPositivo()
        texto = pedirTexto()
        if validarNumero(numero):
            print("El numero es valido")
        if validarTexto(texto):
            print("El texto es valido")
    except TypeError as error:
        print(f"Error: {error}")
    except ValueError as error:
        print(f"Error: {error}")
        
        

main()