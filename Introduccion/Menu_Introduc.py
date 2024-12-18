import os
import base64
from Crypto.Util.number import *
from Xor_operaciones import *
from Conversor_Ascii import *
from BasesNumero     import *


MENU="""
-------------------------Introducion-------------------
    A- ASCII(Convertir Digitos Codigo ASCII,Decifrar mensaje)
    B- Desencriptar mensaje en una base de numeros determinada: 
    C- Desencriptacion XOR 
        -Desencriptacion 
        -Resolver ecuacion XOR
        -Fuerza bruta 
    S- Salir del programa 
    Ingrese Con que le gustaria trabajar: """
SUBMENU1="""            
------------------------Conversor ASCII----------------------
    1. Convertir Digitos Codigo ASCII
    2. Decifrar mensaje
    3. Volver al menu principal
    Ingrese Opcion: """
SUBMENU2=""" 
-------------------Desencriptacion Base de numeros-----------
    1. Base 8  (octal)
    2. Base 10 (Decimal)
    3. Base 16 (Hexadecimal)    
    4. Base 64 (Codificacion Simbolica)
    5. Volver al menu principal
    Ingrese Base: """
SUBMENU3=""""        
---------------------XOR y Fuerza Bruta-----------------
    1. Desencriptacion 
    2. Resolver ecuacion XOR
    3. Desencriptacion por Fuerza bruta
    4. Volver al menu principal
Ingrese su opcion:  """


def Validacion(mensaje,valores):
    """
    Metodo para validar las entradas del usuario
    """
    while True :
        opcion=input(mensaje).strip()
        os.system("cls") 
        if opcion in valores:
            return opcion
        else:
            print("Opcion no valida")

#Opciones---------------------------------------------
def SeleccionBase (mensaje,valores):
    """
    Esta función se encarga de llamar La funcion q atienda lo requerido
    """
    Base=Validacion(mensaje, valores)
    os.system("cls")#Limpia Pantalla
    if  (Base == 1):
        Opcion_octal()
    elif(Base == 2):
        Opcion_decimal()
    elif(Base == 3):
        Opcion_hexadecimal()
    elif(Base == 4):
        Opcion_base64()


def SeleccionAscii (mensaje, valores):
    """
    Esta función se encarga de llamar La funcion q atienda lo requerido
    """
    Base=Validacion(mensaje, valores)
    if (Base == 1):
        Opcion_1()
    elif(Base == 2):
        Opcion_2()


def SeleccionAta (mensaje, valores):
    """
    Esta función se encarga de llamar La funcion q atienda lo requerido
    """
    Base=Validacion(mensaje, valores)
    if  (Base == 1):
        DesencriptacionXOR_Con_Clave()
    elif(Base == 2):
        Ecuacion_XOR()
    elif(Base == 3):
        Desencripcion_Fuerza_Bruta ()
#----------------------------------------------------


def Menu ():
    """
    Funcion que muestra el menu del Programa 
    """

    while True:
        op=Validacion(MENU,{"A","B","C","S"})
        if(op in "Ss"):
            print("Gracias por Usar el programa ")
            break
        if  (op in "Aa"):
            SeleccionAscii(SUBMENU1,{"1","2","3"})
        elif(op in "Bb"):    
            SeleccionBase(SUBMENU2,{"1","2","3","4","5"})
        elif(op in "Cc"):
            SeleccionAta(SUBMENU3,{"1","2","3","4"})



Menu()