#import pandas as pd
#import textual as te
#import numpy as np

def entrada_seleccion_int(x, mensaje="Texto de ejemplo"):
    while True:
        try: entrada = int(input(mensaje))
        except ValueError: print("Error, escriba un número en las opciones de arriba.")
        else:
            if entrada in range(1,x+1):
                return entrada
            else: print("No hay una opción con ese número, intente otro.")

def entrada_alfa(mensaje="Texto de ejemplo 2"):
    while True:
        entrada = input(mensaje)
        entrada = entrada.split()
        alfa = True
        for x in entrada:
            if not x.isalpha():
                alfa = False
                print("Error, asegurese de solo escribir letras")
                break
        if alfa == True: return " ".join(entrada)
            
def entrada_rut(mensaje="Ingresar rut sin guiones ni puntos: "):
    while True:
        entrada = input(mensaje)
        entrada = entrada.upper()
        if len(entrada) <= 9:
            if entrada[0:-1].isnumeric() and (entrada[-1].isnumeric() or entrada[-1] == "K"):
                return entrada[0:-1] + "-" + entrada[-1]
            else:
                print("Rut invalido, asegurese de haberlo escrito bien")
        else:
                print("Rut invalido, asegurese de haberlo escrito bien")

mirut = entrada_rut()
print(mirut)