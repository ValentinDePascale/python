tope = int(input("Ingrese un numero tope: "))
lista = []
for i in range (tope):
    if i % 3 == 0:
        if i % 2 == 0:
            lista.append(i)
print(lista)
