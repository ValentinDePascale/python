def verificarEntero(mensaje:str)->int:
    esValido = False
    while not esValido:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                esValido = True
        except ValueError:
            print("Mal ingreso. Ingrese un numero entero positivo")
    return numero

A = verificarEntero("Ingrese el numero A (inicio): ")
B = 0
while B < A:
    B = verificarEntero("Ingrese el numero B (final): ")
X = verificarEntero("Ingrese el numero X: ")
listaMultiplos = []
for i in range (A, B+1):
    if i % X == 0:
        listaMultiplos.append(i)

print(f"Los multiplos de {X} entre {A} y {B} son: {listaMultiplos}",) 
