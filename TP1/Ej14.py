def contarVocales(texto:str)->int:
    cont = 0
    for i in texto.lower():
        if i in "aeiou":
            cont = cont + 1
    return cont

texto = input("Ingrese una cadena de texto")

vocales = contarVocales(texto)

print(f"La cadena de texto tiene {vocales} vocales")