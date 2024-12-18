import os
import base64
from Aritmetica_Modular import * 
from sympy import isprime



MENU="""
----------------------Aritmetica Modular----------------------
    A-Calcular el MCD (gdc) entre a y b
    B-Cálculo de residuos modulares
    C-Teorema de Fermat 
    D-Inverso modular
    E-Residuo Cuadratico
    F-Legrene Symbol
    G-Algoritmo Tonelli Shaks
    H-Teorema_Chino_Resto
    I-Decifrar Mensaje
    J-Encriptar matematica
    K-Resolver Ecuacion
    S- Salir del programa 
    Ingrese Con que le gustaria trabajar: """
SUBMENU1="""            
------------------------MCD(GDC)----------------------
    1.MCD entre 2 valores 
    2.MCD extendido usando Bezout (devuelve los x e y el mcd)
    Ingrese Opcion: """
SUBMENU2=""" 
----------------Residuo modular------------------------
-El módulo debe ser mayor que cero
-Solo numeros enteros:
"""




#Validacion ----------------------------------------
def Validacion(mensaje, opciones):
    """
    Metodo para validar las entradas del usuario
    """
    while True :
        opcion=input(mensaje).strip().upper()
        if opcion in opciones:
            return opcion
        print("Opción no válida. Intente de nuevo.")


def Verificar_Base(mensaje):
    """
    Esta funcion se encarga de verificar q la opcion cumpla lo establecido  en base a el tipo q sea:
    opcion A
        -  opcion entre  1 y 2
        - ser solo un caracter
    opcion B
        - opcion entre  1 y 4
        -- ser solo un caracter
    Opcion C
        - opcion entre 1 y 3
        - ser solo un caracter
    """


    while True:        
        try:
            numero = int(input(mensaje))
            if numero <= 0:
                raise ValueError("El número debe ser mayor que cero.")
            return numero
        except ValueError as e:
            print(f"Entrada inválida: {e}")  
#---------------------------------------------------







#Opciones-------------------------------------------------------------
def SeleccionMCD ():
    """
    Esta función se encarga de llamar La funcion q atienda lo requerido
    """
    opcion = Validacion(SUBMENU1, {"1", "2", "S"})
    if opcion == "S":
        return 0
    a = Verificar_Base("Ingrese el primer número: ")
    b = Verificar_Base("Ingrese el segundo número: ")
    if opcion == "1":
        print(f"MCD({a} y {b}): {mcd_iterativo(a, b)}")
    elif opcion == "2":
        mcd, x, y = mcd_extendido(a, b)
        print(f"MCD({a}, {b}): {mcd}, coeficientes: x={x}, y={y}")


def Modulares():
    coef=[]
    mod =[]
    totalC=Verificar_Base("Ingrese cantidad de coeficientes y modulos a ingresar: ")
    os.system("cls")#Limpia Pantalla
    print(SUBMENU2)
    for i in range(totalC):
        coef.append(Verificar_Base(f"Ingrese el coeficiente {i + 1}: "))
        mod.append(Verificar_Base(f"Ingrese el módulo {i + 1} "))
    r=Residuo_modular(coef,mod)
    os.system("cls")#Limpia Pantalla
    print("Resultados de los residuos modulares:")
    for i, res in enumerate(r, start=1):
        print(f"Residuo {i}: {res}")


def Fermat():
    while(True):
        coef1=Verificar_Base("Ingrese el primer coeficiente: ")
        coef2=Verificar_Base("Ingrese el segundo coeficiente (debe ser primo): ")
        if isprime(coef2):
            print(f"Resultado: {teorema_fermat(coef1, coef2)}")
        else:
            print("El segundo coeficiente debe ser un número primo.")


def Inverso():
    while(True):
        a=Verificar_Base("Ingresa el valor:   ")
        r=Verificar_Base("Ingresa el residuo: ")
        m=Verificar_Base("Ingresa el modulo:  ")
        if(mcd_iterativo(a,m) % r != 0):
            print("No se puede encontrar el valor ")
        else:
            print(f"Inverso modular: {InversoModular(a, r, m)}")


def Residuo():
    while(True):
        vect =[]
        total=Verificar_Base("Ingrese cantidad a ingresar: ")
        p=Verificar_Base("Ingrese modulo: ")
        os.system("cls")#Limpia Pantalla
        for i in range(total):
            vect.append(Verificar_Base("Ingrese modulo: "))
        print("Residuos: ",residuo_Cuadratico(vect,p))


def LegrengeS():
    while(True):
        ints =[]
        total=Verificar_Base("Ingrese cantidad a ingresar: ")
        p=Verificar_Base("Ingrese modulo: ")
        os.system("cls")#Limpia Pantalla
        for i in range(total):
            ints.append(Verificar_Base("Ingrese valor: "))
        print("residuo cuadratico: ",Legrenge_symbol(ints,p))


def Tonelli_shaks():
    while(True):
        a=Verificar_Base("Ingrese valor: ")
        p=Verificar_Base("Ingrese modulo: ")
        os.system("cls")#Limpia Pantalla
        print("La raiz mas chica es: ",tonelli_shanks (a,p))


def Teorema_Chino_Resto():
    restos=[]
    divisores=[]
    total=Verificar_Base("Ingrese cantidad a ingresar: ")
    for i in range(total):
        restos.append(Verificar_Base("Ingrese resto ",(i+1),": "))
        divisores.append(Verificar_Base("Ingrese divisor ",(i+1),": "))
    if (Chinise_Reminder(divisores,restos)== -1):
        print("No existe solucion")
    else:
        print("Solucion: ",Chinise_Reminder(divisores,restos))


def Desenc ():
    vect=[]
    cant=Verificar_Base("Ingrese cantidad de valores: ")
    p=Verificar_Base("Ingrese modulo: ")
    for i in range(cant):
        vect.append(Verificar_Base("Ingrese valor: "))
    print("Mensaje: ",long_to_bytes(Desencriptacion(vect, p )).decode())


def Encri():
    FLAG = b'crypto{????????????????????}'
    encriptar_M(FLAG)


def Ecuacion():
    n=Validacion("Ingrese un valor: ")
    e1=Validacion("Ingrese un valor: ")
    e2=Validacion("Ingrese un valor: ")
    c1=Validacion("Ingrese un valor: ")
    c2=Validacion("Ingrese un valor: ")
    Equacion (n,e1,e2,c1,c2)

#---------------------------------------------------------------------

def Menu ():
    """
    Funcion que muestra el menu del Programa 
    """
    while True:
        os.system("cls")  # Limpia la pantalla
        op = Validacion(MENU, {"A", "B", "C", "D", "E","F","G","H","I","J", "S"})
        if(op in "Ss"):
            print("Gracias por Usar el programa ")
            break
        elif(op == "A"):
            return SeleccionMCD(Verificar_Base(1))
        elif(op == "B"):
            Modulares()
        elif(op == "C"):
            Fermat()
        elif(op == "D"):
            Inverso()
        elif(op == "E"):
            Residuo() 
        elif(op == "F"):
            LegrengeS()
        elif(op == "G"):
            Tonelli_shaks()
        elif(op == "H"):
            Teorema_Chino_Resto()
        elif (op == "I"):
            Desenc()
        elif op == "J" :
            Encri()
        elif(op == "K"):
            Ecuacion()




Menu()