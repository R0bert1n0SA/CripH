
import os
import base64
from Crypto.Util.number import *

MO="""-------------------Ingreso de cadena----------------------
Tener en cuenta
    - numeros de 1 digito octal agregar 2 ceros Ej: 4  --> 004
    - numeros de 2 digitos octal agregar 1 cero Ej: 23 --> 023 
Ingrese la cadena a decifrar:  """
MD="""-------------------Ingreso de cadena---------------------- 
Ingrese la cadena a decifrar:  """
M64="""¡Si ingresa una cadena Hexadecimal la decodificacion estara errada!
            Ingrese la cadena a decifrar en base 64: """
TABLA_BASE64 = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
        "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15,
        "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
        "Y": 24, "Z": 25, "a": 26, "b": 27, "c": 28, "d": 29, "e": 30, "f": 31,
        "g": 32, "h": 33, "i": 34, "j": 35, "k": 36, "l": 37, "m": 38, "n": 39,
        "o": 40, "p": 41, "q": 42, "r": 43, "s": 44, "t": 45, "u": 46, "v": 47,
        "w": 48, "x": 49, "y": 50, "z": 51, "0": 52, "1": 53, "2": 54, "3": 55,
        "4": 56, "5": 57, "6": 58, "7": 59, "8": 60, "9": 61, "+": 62, "/": 63
        }



def ValidarDiv(mensaje,div,valor,Error,base):
    cadena=input(mensaje)
    if base == 64:           
        if(len(cadena) == 1):
            print("Longitud invalida debe ser de mas de un caracter")
            return 0,cadena
        elif(len(cadena) % div != valor):
            cadena += "=" * (div-(len(cadena) % div)) 
        return 1,cadena
    
    if(len(cadena) % div != valor):
        os.system("cls" if os.name == "nt" else "clear")
        print(Error)
        return 0,cadena
    return 1, cadena


def EvaluarLongitud(base):
    """
    Función que evalúa Logitud de cadena dependiendo base :
    1) Si es Octal        -> longitud debe ser multiplo de 3
    2) Si es Hexadecimal  -> longitud debe ser multiplo de 2
    3) Si es Base64       -> longitud mas de un caracter ysi no es multiplo de 4 se le agrega = hasta sea multiplo
    """
    if base == 8:
        return ValidarDiv(MO,3,0,"La cadena debe ser multiplo de 3 faltan numeros",base)
    elif base == 16:
        return ValidarDiv("Ingrese la cadena a decifrar: ",2,0,"Longitud invalida debe ser par",base)
    elif base == 64:
        return ValidarDiv(M64,4,0,"Longitud invalida debe ser de mas de un caracter",base)
    elif base == 10:
        cadena=input(MD)
        return 1,cadena


def CadenaValid(Base,valores):
    """
    Funcion que permite evaluar q una cadena ingresada sea valida
        arg:recibe la base y en base a ella evalua sus condiciones
        Ret: retorna la cadena valida 
    """
    flag=1
    while True:
        flag,cadena=EvaluarLongitud(Base)               
        if flag == 1:
            try:
                for caracter in cadena:
                    if caracter not in valores:
                        raise ValueError
                return cadena
            except ValueError:
                os.system("cls" if os.name == "nt" else "clear") 
                print ("CADENA INVALIDA")


def Correccion(cadena,Array,div,base):
    """
    Funcion para realizar una correccion para la cadena poder interpretarla  correctamente
        args: recibe la cadena a convertir, el Array donde se guardara los resultados intermedios,
            el divisor del numero entero y la base a utilizar
        Ret: devuelve el array con los resultados intermedios
    """
    iteraciones = len(cadena) // div
    for i in range(iteraciones):
        valor=((cadena[i*div:(i+1)*div]))
        numero=int(valor,base)
        Array.append(numero)
    return Array



def Opcion_octal():
    cadena=CadenaValid("01234567",8)
    octales = []
    octales=Correccion(cadena,octales,3,8)
    MensajeDesencriptado(octales)


def Opcion_decimal():
    cadena=CadenaValid("1234567890",10)
    print(cadena,"-->",long_to_bytes(int(cadena)))
    print(long_to_bytes(int(cadena)).decode("utf-8"))


def Opcion_hexadecimal():
    cadena=CadenaValid("0123456789ABCDEFabcdef",16) 
    Hexadecimales=[]
    Hexadecimales=Correccion(cadena,Hexadecimales,2,16)
    print(Hexadecimales)
    MensajeDesencriptado(Hexadecimales)


def Opcion_base64():
    cadena=CadenaValid("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/=",64)
    print(base64.b64decode(cadena).decode("utf-8",'ignore'))


def MensajeDesencriptado(Array):
    """
    Funcion que convierte un mensaje codificado en binario a ASCII
        args: recibe el array de numeros binarios y desencripta valor por valor
    """
    os.system("cls" if os.name == "nt" else "clear")
    mensaje=""
    for i in Array:
        mensaje+=chr(int(i))
    print("Mensaje: " ,mensaje)





