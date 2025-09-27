def cadena_reversa(texto:str):
    print(f"Texto invertido: {texto[::-1]}")

def palindromo(texto:str):
    textoInvertido = texto[::-1]
    if texto.lower() == textoInvertido.lower():
        print(f"El texto {texto} es un palindromo{textoInvertido} ")
    else:
        print(f"{texto} no es palindromo")        




texto = input("Ingrese la cadena de texto a invertir: ")
cadena_reversa(texto)
palindromo(texto)