import math 
import operator
import numpy as np
from functools import reduce
from Crypto.Util.number import long_to_bytes
from sympy import symbols, Eq, solve, mod_inverse,linsolve
from random import randint
from Crypto.Util.number import long_to_bytes

def mcd_iterativo(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros usando el algoritmo iterativo de Euclides.
    Args:
        a: El primer número entero.
        b: El segundo número entero.
    Returns:
        El MCD de 'a' y 'b'.
    """
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

def mcd_extendido(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros 'a' y 'b' 
    y encuentra los coeficientes 'x' e 'y' que satisfacen la ecuación de Bézout: a * x + b * y = MCD(a, b).

    Args:
        a: El primer número entero.
        b: El segundo número entero.

    Returns:
        Una tupla que contiene el MCD (en la posición 0), 'x' (en la posición 1) e 'y' (en la posición 2).
    """

    if b == 0:
        return (a, 1, 0)
    (mcd, x1, y1) = mcd_extendido(b, a % b)# avanzo hasta que b sea 0
    x = y1
    y = x1 - (a // b) * y1 
    return (mcd, x, y)

def Residuo_modular(coef,mod):
    """
    Cacula residuo modular  de una ecuacion"
    """
    result=[]
    for i in range(coef.__len__()):
        result.append(coef[i] % mod[i])
    return result

def teorema_fermat(a, p):
    """
    Función para calcular el valor al que hacer módulo con el Pequeño Teorema de Fermat en Python.

    Argumentos:
        a (int): El número entero al que se eleva.
        p (int): Un número primo.

    Retorno:
        int: El valor de a^(p-1) mod p.

    Ejemplo:
        teorema_fermat(7, 17) == 2
    """
    # Elevamos a a la potencia p-1
    resultado= pow(a, p - 1,p)
    return resultado

def InversoModular(a,r,m):
    num=0
    result=0
    while True:
        result=a*num
        if(result % m == r):
            return num
        num+=1
# Condición de escape para evitar un bucle infinito
        if num > m:  # Se evalúa hasta m iteraciones como límite superior
            return "No se encontró solución dentro del rango."

def residuo_Cuadratico(vect,p):
    residuo=[]
    for a in range(358):
        if pow(a,2,p) in vect:
            residuo.append(a)
    return residuo

def Legrenge_symbol(ints,p):
    a = 0
    for i in ints:
        if pow(i,(p-1)//2,p) == 1:
            print(i)
            a = i
            break
    return pow(a,(p+1)//4,p)



def Legrene_symbol_Boolean(a,p):
    if(pow(a,(p-1)//2,p) == 1):
        return True
    else:
        return False

def calcularR(a,p):
    # Step 1: Write p - 1 as q * 2^s, where q is odd
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    z = 2
    while Legrene_symbol_Boolean(z,p):
        z=z+1

    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)

    while True:
        taux = t
        i = 0
        for i in range(m):
            if taux == 1:
                break
            taux = pow(taux, 2, p)

        if i == 0:
            return [r,p-r]

        b = pow(c, pow(2 ,(m - i - 1)), p)
        c = (b * b) % p
        r = (r * b) % p
        t = (t * c) % p
        m = i

def tonelli_shanks (a,p):
    if Legrene_symbol_Boolean(a,p):
        return calcularR(a,p)
    else:
        return None


def Chinise_Reminder(divisores,restos):
    """Resuelve un sistema de congruencias utilizando el Teorema Chino del Resto.

    Args:
        modulos: Una lista con los módulos de las congruencias.
        restos: Una lista con los restos correspondientes.

    Returns:
        La solución del sistema de congruencias.
    """

    # Verificar que las listas tengan la misma longitud
    if len(divisores) != len(restos) and (math.gcd(divisores)==1):
        raise ValueError("Las listas de módulos y restos deben tener la misma longitud.")
    else:
        if(reduce(math.gcd,divisores)==1):
        # Calculamos el producto de los divisores
            producto = reduce(operator.mul, divisores)
        # Generamos Los N sub i
            resultado = [producto // num for num in divisores]
        #Inversos Modulares
            inversos=[]
            for i in range(len(divisores)):
                t=False
                y=1
                while (t == False):
                    if((resultado[i]*y % divisores[i])==1):
                        inversos.append(y)
                        t=True
                    else:
                        y=y+1
            solucion=0
            for i in range(len(divisores)):
                solucion=solucion +(restos[i]*resultado[i]*inversos[i])
            return solucion % producto
        else:
            return -1


def Desencriptacion(dato,p):
    cadena=[]
    for element in dato:
        cadena.append(str(int(Legrene_symbol_Boolean(element,p))))
    return int(''.join(cadena),base=2)



def encriptar_M(flag):
    a = 288260533169915
    p = 1007621497415251


    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext

def Equacion (n,e1,e2,c1,c2):
    lado_izquierdo1 = pow(c1, e2, n)  # Eleva c1 a e2 módulo n
    lado_izquierdo2 = pow(c2, e1, n)  # Eleva c2 a e1 módulo n

    # Calcula las potencias para los factores del lado derecho de las ecuaciones:
    factor_derecho1 = pow(5, e1 * e2, n)  # Eleva 5 a la potencia combinada de los exponentes
    factor_derecho2 = pow(2, e1 * e2, n)  # Eleva 2 a la potencia combinada de los exponentes

    # Calcula la diferencia modular que contiene información sobre p y q:
    diferencia_modular = (lado_izquierdo1 * factor_derecho1 - lado_izquierdo2 * factor_derecho2) % n

    # Usa el Máximo Común Divisor (GCD) para extraer uno de los factores primos:
    q = math.gcd(diferencia_modular, n)  # Calcula el GCD entre la diferencia y n
    p = n // q  # Calcula el otro factor dividiendo n por q

    # Imprime los resultados en formato descriptivo:
    print('crypto{' + str(p) + ', ' + str(q) + '}')