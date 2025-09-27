cant = 0
masAlto = 0
venta = 1
total = 0
while venta > 0:
    venta = int(input(f"Ingrese el monto de la venta {cant+1}: "))
    if venta > 1:
        if venta > masAlto:
            masAlto = venta
        cant = cant + 1
        total = total  + venta

promedio = total / cant
print(f"Total de ventas: {cant}")
print(f"Mas alta: {masAlto}")
print(f"Promedio: {promedio}")
print(f"Total recaudado: {total}")


