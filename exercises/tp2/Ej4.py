def verificar_entero(mensaje:str)->int:
    esValido = False
    while not esValido:
        try:
            entero = int(input(mensaje))
            if entero > 0:
                esValido = True
            else: 
                print(f"Mal ingreso. Por favor, {mensaje}")
        except ValueError:
            print(f"Mal ingreso. {mensaje}")
    return entero

def mayorDigito(lista:list)->int:
    digito_mayor = lista[0]
    for i in range (len(lista)):
        if lista[i] > digito_mayor:
            digito_mayor = lista[i]
    return digito_mayor

# def contarDigitos(numero:int)->int:
#     cont = 0
#     while numero > 0:
#         cont += 1
#         numero = numero // 10
#     return cont

numero = verificar_entero("Ingrese un entero positivo: ")
lista = []
for i in str(numero):
    lista.append(i)

print(lista)

digito_mayor = mayorDigito(lista)
print(f"El mayor digito es {digito_mayor} en el indice {lista.index(digito_mayor)}")


# digitos = contarDigitos(numero)
# print(f"El numero {numero} tiene {digitos} digitos")