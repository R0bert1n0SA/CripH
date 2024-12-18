from pwn import *
from binascii import *

MECU="""-------------------Ingreso de Valores----------------------
Tener en cuenta
    - El Valor Debe Hexadecimal
    - La longitud debe ser par"""
FB  ="""-------------------Ingreso Cadena--------------------------
Tener en cuenta
    - Menor a 100 caracteres
    - Debe ser Hexadecimal"""
MOP ="""-----------------Seleccion de metodo------------------
    1.fuerza bruta simple
    2.fuerza bruta Con llave parcial"""

def DesencriptacionXOR_Con_Clave():
    """
    Funcion Desencripta mensaje  con una clave mediante XOR operation
    """
    def Operacion_xor2(dato,num):
        """
        Función que realiza la operación xor entre dos hexadecimales
            Arg:
                dato  (str) : cadena a desencriptar
                num   (int) : numero con q se desencriptara
        """
        flag=''
        for c in dato:
            flag += chr(ord(c) ^ num) #Operador XOR (ord conviete un str/byte a un int)
        print('{}'.format(flag))#Imprime El mensaje descifrado
    
    cadena=input("Ingrese una cadena a desencriptar con xor :")
    num=input("Ingrese Llave de desencriptacion: ")
    Operacion_xor2(cadena,num)


def Ecuacion_XOR():
    """
    Funcion resuelve una ecuacion Hexadecimal con valores del usuario
    """
    def Validar(Valores):
        """
        Validez de Numeros ingresados:
        1. Son numeros Hexadecimales
        2. longituda de los mismos debe ser par 
        Parametros:
            valores : (list): lista de numeros vacia
        Retorno:
            valores : (list): lista de numeros 
        """
        print(MECU)
        for ite in range(0,4):
            while True:
                valor=(input(f"Ingrese el valor{ite + 1} : "))
                if(len(valor) % 2 == 0):
                    if all(c in "0123456789ABCDEFabcdef" for c in valor):                      
                        Valores.append(valor)      
                        break
                    else:
                        print("ERROR:No es hexadecimal")
                else:
                    print("ERROR: La longitud debe ser Par")
        return Valores

    Valores=[]
    Valores= Validar(Valores)
    a            =Valores[0]
    bXORa        =Valores[1]
    bXORc        =Valores[2]
    dXORaXORbXORc=Valores[3]
    print(f"""
    Ecuacion :
    A             = {a}
    B ^ A         = {bXORa}
    B ^ C         = {bXORc}
    D ^ A ^ B ^ C = {dXORaXORbXORc}
    """)
    a = bytes.fromhex(a)
    b = xor(a, bytes.fromhex(bXORa))
    c = xor(b, bytes.fromhex(bXORc))
    d = xor(a, c , b, bytes.fromhex(dXORaXORbXORc))
    print("A =",a,"\n B= ",b," \n C=",c,"\n D= ",d)


def Desencripcion_Fuerza_Bruta ():
    """
    Funcion q desencripta mensaje con 2 varaciones de fuerza bruta
    1- Fuerza Bruta Simple
    2- Fuerza Bruta Con CLave Parcial
    """
    def opcionAta ():
        """
        Validacion de opcion de metodode traduccion:
            1- Fuerza Bruta Simple
            2- Fuerza Bruta Con CLave Parcial
        Retorno:
            Opcion: Numero correspondiente a la opcion elegida por el usuario
        """
        while True:
            Opcion=input(MOP)
            if len(Opcion) == 1 and (Opcion  in  "12"):
                return  Opcion
            elif len(Opcion) > 1 :
                print ("Opcion no clara")
            else:
                print("Error: Opcion no valida")


    def Validar():
        ''' 
        Funcion que valida la entrada del usuario
            -Tamañio menor a 100 caracteres por eficiencia
            -Sea Hexadecimal
        Retorno:
            La cadena valida
        '''
        print(FB)
        while True:
            Dato=(input("Ingrese cadena: "))
            if(len(Dato) > 100): #Si el tamaño de la cadena es mayor a 100 Caracteres
                print("La cadena es demaciado extensa ")
            else:
                if all( c in "0123456789ABCDEFabcdef" for c in Dato):# Si todos los elementos son hexadecimales
                    return Dato
                else: 
                    print("ERROR: No es Hexadecimal")


    def ComparadoBitPorBit(dato,key):
        """
        Compara dos cadenas Bit Por Bit
        Parametros:
            -dato: Cadena a comparar
            -key: Clave para comprobar si coincide con la primera
        Retorno:
            -mensaje (str): si se pudieron decofificar todos los bytes
            -str de error
        """
        mensaje=b''
        for b1, b2 in zip(dato, key):#comparo En simultanio bit a bit
            mensaje += bytes([b1 ^ b2])
        try:
            return mensaje.decode('utf-8') #Verifico
        except:
            return "Algunos bytes no se pudieron decodificar"


    def Fuerza_Bruta_simple(Dato):
        """
        Metodo de fuerza bruta simple
        Se itera sobre todas las posibles claves y comprueba si coinciden con la entrada del usuario
        Parametros:
            -Dato: El dato que se quiere descifrar
        """
        Dato = bytes.fromhex(Validar()) #Convierte el texto a Bytes
        Comparador=input("Ingrese comparador (Frase o palabra)  con la q deberia iniciar la contraseña: ")
        for i in range(256):  #Recorro todos Los valores de un Byte  (de 0 a 255)
            salida=b""
            for elem in  Dato :  #recorremos cada byte de la cadena
                salida += bytes([elem ^ i]) #aplicamos XOR con la llave y lo agregamos al resultado   
                if Comparador in str(salida) : #verifica si encotro la contraseña 
                    print(salida.decode("utf-8")) #retornamos en formato string
        if( i == 255):
            print("La cadena no pudo ser decifrada ")


    def Fuerza_Bruta_Con_ParcialKey(Dato):
        """
        Metodo de fuerza bruta Con Parcial Key
        Se toma una parte de la clave como referencia y se busca en todo el rango de combinaciones
        de bits posibles
        Parametros:
            -Dato: El dato que se quiere descifrar
        """
        #Obtener la key para desencriptar  
        Dato = bytes.fromhex(Validar()) #Convierte el texto a Bytes
        key=input("Ingrese Clave para intentar Ataque: ").encode()
        long=len(key)
        salida=(ComparadoBitPorBit(Dato[:long],key) + "t").encode('utf-8')
        salida += salida * int((len(Dato) - len(salida))/len(salida))# Aumentamos la la longitud para q sea igual a la de Dato
        salida += salida[:((len(Dato) -len(salida))%len(salida))] # Ajustar la clave final para que su longitud sea exactamente igual a la longitud del Dato 
        print (ComparadoBitPorBit(Dato,key))

    op=(opcionAta())
    if(op == 1):
        Fuerza_Bruta_simple()
    else:    
        Fuerza_Bruta_Con_ParcialKey()   









