def cadena_reversa():
    texto = input("Ingrese la cadena de texto a invertir: ")
   # print(f"Texto invertido: {texto[::-1]}")
    lista = []
    lista.append(texto)
   
    iterador_inverso = reversed(lista)
    nueva_lista = list(iterador_inverso)

    print(lista)



cadena_reversa()