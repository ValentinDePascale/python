nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print(f"Hola {nombre}, tienes {edad} y eres mayor de edad")
else:
    print(f"Hola {nombre}, tienes {edad} y eres menor de edad")