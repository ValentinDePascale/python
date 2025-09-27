diccionario = {
    "amor": "Sentimiento profundo de afecto y cariño hacia alguien o algo.",
    "amigo": "Persona con la que se mantiene una relación de afecto, confianza y compañerismo.",
    "barco": "Vehículo que se utiliza para navegar por el agua.",
    "biblioteca": "Lugar donde se guardan y prestan libros.",
    "casa": "Edificio o construcción destinado a ser habitado.",
    "cielo": "Espacio en el que se mueven los astros y que se observa desde la Tierra.",
    "computadora": "Máquina electrónica que recibe y procesa datos para convertirlos en información.",
    "duda": "Incertidumbre sobre qué pensar, creer o hacer.",
    "deseo": "Ganas de conseguir o experimentar algo.",
    "elefante": "Animal mamífero de gran tamaño, con trompa y colmillos.",
    "estrella": "Cuerpo celeste que brilla con luz propia en el universo.",
    "fuego": "Fenómeno de combustión que produce luz y calor.",
    "felicidad": "Estado de ánimo de satisfacción, alegría o bienestar.",
    "gato": "Animal mamífero doméstico, ágil y de carácter independiente.",
    "guitarra": "Instrumento musical de cuerdas que se toca con los dedos o con púa.",

}
def validarInicial (mensaje)->str:
    unCaracter = False
    while not unCaracter:
        try:
            inicial = input(mensaje)
            if len(inicial) == 1 and inicial.lower() in "abcdefghijklmopq":
                unCaracter = True
            else:
                print("Usted ingreso mas de 1 caracter")    
        except TypeError:
            print("Mal ingreso"+mensaje)
    return inicial



inic = validarInicial("Ingrese una letra: ")

lista_palabras = [i for i in diccionario if i[0]== inic]

print(lista_palabras)
