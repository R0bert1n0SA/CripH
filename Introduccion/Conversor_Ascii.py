import os

def PedirNumero(flag):
    while True:
        try:
            numero = int(input("Ingrese un número: "))  
            if flag == 1:          
                if numero >=32  and numero <= 127:
                    return numero
                else:
                    print("El número debe estar en la tabla ASCII rango  de 32 a 127.")
            else:
                return numero
        except ValueError:
                print ("Usted ingreso un valor no entero")


def CargaValores(Valores,Flag):
    iterador=input("Cuantos numeros va ingresar: ")
    for  i in range(int(iterador)):
        num = PedirNumero(Flag)
        Valores.append(num)


def Opcion_1():
    Valores=[]
    CargaValores(Valores,1)
    for elmento in Valores:
        print("Numero:",elmento,"Caracter --> ",chr(elmento) )


def Opcion_2():
    def Verificar():
        while(True):
            try:
                Clave=int(input("Digite una clave de cifrado xor:  "))
                return Clave
            except ValueError:
                print ("Usted ingreso un valor no entero")

    Valores=[]
    Clave=Verificar()
    CargaValores(Valores,0)
    print("".join(chr(elmento ^ Clave) for elmento in Valores))









