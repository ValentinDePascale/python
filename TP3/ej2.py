def verificarEntero(mensaje:str)->int:
    esValido = False
    while not esValido:
        try:
            entero = int(input(mensaje))
            if entero > 0:
                esValido = True
            else:
                print(f"Mal ingreso. {mensaje}")
        except ValueError:
            print(f"Mal ingreso. {mensaje}")
    return entero

nombres_mixtos = ["Tomás", "Ana", "Lautaro", "Paula", "Federico", "Milagros", "Ramiro", "Victoria", "Santiago", "Abril"]

longitud = verificarEntero("Ingrese longiutd: ")

nueva_lista = [i for i in nombres_mixtos if len(i) >= longitud]

print(nueva_lista)
