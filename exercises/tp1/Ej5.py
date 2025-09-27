texto = input("Ingrese una cadena de texto: ")
cont = 0
for i in texto:
    if i == " ":
        cont += 1

print(f"Contiene {cont} espacios")

#Tambien, se puede hacer con el método espacios = texto.count(" ")