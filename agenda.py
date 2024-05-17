import pandas as pd
from os import system, name
#import textual as te
#import numpy as np

RUN = True
if name == "nt":
    CLEAR = "cls"           # EN WINDOWS
else:
    CLEAR = "clear"         # EN OTROS SISTEMAS OPERATIVOS
#-----------------------------------------------------------------------------------------
# FUNCIONES DE ENTRADA
#-----------------------------------------------------------------------------------------
def entrada_seleccion_int(x, mensaje="Elige una opcion: "):
    while True:
        try: entrada = int(input(mensaje))
        except ValueError: print("Error, escriba un número en las opciones de arriba.")
        else:
            if entrada in range(1,x+1):
                return entrada
            else: print("No hay una opción con ese número, intente otro")

def entrada_alfa(mensaje="Ingresar palabras: "):
    while True:
        entrada = input(mensaje)
        entrada = entrada.split()
        alfa = True
        for x in entrada:
            if not x.isalpha():
                alfa = False
                print("Error, asegurese de escribir solo letras o espacios")
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
                print("Rut invalido, asegurese de haber escrito bien el rut")
        else:
                print("Rut invalido, asegurese de haber escrito bien el rut")

def entrada_numero(mensaje="Ingrese un numero: "):
    while True:
        try: entrada = int(input(mensaje))
        except ValueError: print("Error, asegurese de ingresar solo numeros enteros")
        else: return entrada

def entrada_alfanumerico(mensaje="Ingresa algo: "):
    while True:
        entrada = input(mensaje)
        entrada = entrada.split()
        alfanum = True
        for x in entrada:
            if not x.isalnum():
                alfanum = False
                print("Error, Evite usar guiones, comas, puntos u otros simbolos")
                break
        if alfanum: return " ".join(entrada)
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# ARCHIVO DE DATOS
#-----------------------------------------------------------------------------------------
try: df = pd.read_csv("contactos.csv")
except FileNotFoundError:
    f = open("contactos.csv", "w")
    f.write("Nombres,ApellidoPaterno,ApellidoMaterno,NumeroTelefono,Direccion,RUT")
    f.close()
    df = pd.read_csv("contactos.csv")
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# MENUS Y FUNCIONES PRINCIPALES
#-----------------------------------------------------------------------------------------
def main_menu():
    system(CLEAR)
    print("Que quiere hacer?")
    print("1- Ver contacto\n2- Añadir contacto\n3- Eliminar contacto\n4- Editar contacto\n5- Buscar contacto\n6- Cerrar agenda")
    seleccion = entrada_seleccion_int(6)
    return seleccion

def ver_contactos():
    while True:
        system(CLEAR)
        if df.index.empty:
            print("No hay ningún contacto agregado")
            back = entrada_alfa('Escriba "volver" para regresar al menú principal: ')
            if back.upper() == "VOLVER":
                return
        else:
            print(df)
            back = entrada_alfa('Escriba "volver" para regresar al menú principal: ')
            if back.upper() == "VOLVER":
                return

def aniadir_contacto():
    system(CLEAR)
    Nombres = entrada_alfa("Ingrese el nombre o los nombres del contacto: ")
    ApellidoP = entrada_alfa("Ingrese el primer apellido del contacto: ")
    ApellidoM = entrada_alfa("Ingrese el segundo apellido del contacto: ")
    NumeroTelefono = entrada_numero("Ingrese el numero telefónico del contacto: ")
    Direccion = entrada_alfanumerico("Ingrese la dirección del contacto: ")
    Rut = entrada_rut("Ingrese el RUT del contacto: ")
    nuevo_contacto = [Nombres,ApellidoP,ApellidoM,NumeroTelefono,Direccion,Rut]
    df.loc[len(df)] = nuevo_contacto
    df.to_csv("contactos.csv")
    print("Su contacto ha sido añadido exitosamente.")
    while True:
        back = entrada_alfa('Escriba "volver" para regresar al menú principal: ')
        if back.upper() == "VOLVER":
            return
#-----------------------------------------------------------------------------------------

while RUN:
    main_select = main_menu()
    if main_select == 1:
        ver_contactos()
    if main_select == 2:
        aniadir_contacto()