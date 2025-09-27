def palabraLarga(texto:str)->str:
    palabrasSeparadas = texto.split()
    palabrasSeparadas.sort(key=len)
   
    return palabrasSeparadas[-1]

texto = input("Ingrese una cadena de texto: ")
palabra = palabraLarga(texto)
print(f"La palabra mas larga de la cadena es {palabra}, tiene {len(palabra)} letras")