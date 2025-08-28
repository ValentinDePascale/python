def contarCaracteres(oracion:str)->int:
    
    return len(oracion)

def contarLetras(oracion:str)->int:
    letras = 0
    for i in oracion.lower():
        if i.isalpha():
            letras = letras +1
    return letras

def contarEspacios(oracion:str)->int:
    return oracion.count(" ")
oracion = input("Ingrese una oración: ")


print(f"Tiene {contarCaracteres(oracion)} caracteres")
print(f"Tiene {contarLetras(oracion)} letras")
print(f"Tiene {contarEspacios(oracion)} espacios")