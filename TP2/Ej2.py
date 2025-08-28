# def ingreso_dia(mes):
#     diaValido=False
#     while not diaValido:
#         try:
#             dia = int(input("Ingrese el dia: "))
#             if dia > 0 and dia <= 31:
#                 diaValido = True
#         except ValueError:
#             print("Mal ingreso. Intentelo nuevamente")
#     return dia


# def ingreso_mes():
#     mesValido=False
#     while not mesValido:
#         try:
#             mes = int(input("Ingrese el mes (1-12): "))
#             if mes > 0 and mes <= 12:
#                 mesValido = True
#         except ValueError:
#             print("Mal ingreso. Intentelo nuevamente")
#     return mes

def verificacion_anio():
    anioValido=False
    while not anioValido:
        try:
            anio = int(input("Ingrese el año: "))
            if anio > 0:
                anioValido = True
        except ValueError:
            print("Mal ingreso. Intentelo nuevamente")
    return anio

def EsBisiesto(anio):
    esBisiesto = False
    if anio % 4 == 0:
        if anio % 100 != 0 or anio % 400 == 0:
            esBisiesto = True
    return esBisiesto


ingresoAnio = verificacion_anio()
anioBisiestio = EsBisiesto(ingresoAnio)

if anioBisiestio:
    print("Es bisiesto")
else:
    print("No es bisiesto")