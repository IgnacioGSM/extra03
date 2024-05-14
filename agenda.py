import pandas as pd
import textual as te
import numpy as np

def seleccion(x, mensaje="Texto de ejemplo"):
    while True:
        try: elegido = int(input(mensaje))
        except ValueError: print("Error, escriba un número en las opciones de arriba.")
        else:
            if elegido in range(1,x+1):
                return elegido
            else: print("No hay una opción con ese número, intente otro.")