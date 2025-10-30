from abc import ABC

class Vehiculo(ABC):
    def __init__(self, marca:str, modelo:str, patente:str, color:str, anio_fabricacion:int, precio:float, km:float, combustible: str):
        if not isinstance(marca, str) or marca.strip() == "" or marca.isspace():
            raise ValueError("La marca debe ser string valido") 
        if not isinstance(modelo, str) or modelo.strip() == "" or modelo.isspace():
            raise ValueError("El modelo debe ser string valido") 
        if not isinstance(patente, str) or patente.strip() == "" or patente.isspace():
            raise ValueError("La patente debe ser string valido") 
        if not isinstance(color, str) or color.strip() == "" or color.isspace():
            raise ValueError("El color debe ser string valido") 

        if not isinstance(anio_fabricacion, int) or anio_fabricacion <= 0:
            raise ValueError("El año de fabricacion debe ser valido")
        if not isinstance(precio, float) or precio <= 0:
            raise ValueError("El precio debe ser valido")
        if not isinstance(km, int) or km <= 0:
            raise ValueError("El km de fabricacion debe ser valido")
    
        if not isinstance(combustible, str) or combustible.strip() == "" or combustible.isspace():
            raise ValueError("El combustible debe ser string valido") 

        self._marca = marca
        self._modelo = modelo
        self._patente = patente
        self._color = color
        self._anio_fabricacion = anio_fabricacion
        self._precio = precio
        self._km = km
        self._combustible = combustible

    def __str__(self)->str:
        return (
            f"Marca: {self._marca}\n"
            f"Modelo: {self._modelo}\n"
            f"Patente: {self._patente}\n"
            f"Color: {self._color}\n"
            f"Año: {self._anio_fabricacion}\n"
            f"Precio: ${self._precio:.2f}\n"
            f"KM: {self._km}\n"
            f"Combustible: {self._combustible}"
        )
    