import base64
import sys
import time
import math


def basee64(entrada):
    print("Entrada: " + entrada)
    bs64= base64.b64encode(entrada.encode('ascii'))
    print("codigo en base64: " + str(bs64))
    return entrada

def entropias(base,largo):
    print("")
    h=math.log(base, 2)*largo
    print("entropia:" )
    print(h)
    return h

def func_ascii(entrada):
    x=[]
    print("")
    print("Codigo en ascii: " )
    for char in entrada:
        ascii = ord(char)
        x.append(ascii)
        print(str(ascii), end="")   
    return x    

def padding(entrada):
    tamaño= 4*len(entrada)
    equiss=""
    print(equiss.ljust(55-tamaño,"x"))



def hexadec(entrada):
    #entrada = hex(entrada)
    print("")
    N=[]
    print("Hash: ")
    tamaño=0
    for i in range(len(entrada)-1):
        aux=str(hex(entrada[i])) 
        N.append(aux)
        n=str(aux)
        #tamaño= len(n)+tamaño
        print(n, end="")
       
    return N

#Lectura archivos (1 credencial sacada del archivo rockyou.txt)
#1 entrada de texto
#f = open('credencial1.txt')
#line=f.readlines()
#print(line)

#Lectura archivos (10 credenciales sacadas del archivo rockyou.txt)
#10 entradas de texto

#f = open('credenciales10.txt')
#line=f.readlines()
#print(line)

#Lectura archivos (20 credenciales sacadas del archivo rockyou.txt)
#20 entradas de texto

#f = open('credenciales20.txt')
#line=f.readlines()
#print(line)

#Lectura archivos (50 credenciales sacadas del archivo rockyou.txt)
#50 entradas de texto

f = open('credenciales.txt')
line=f.readlines()
print(line)


#Comienza a tomar tiempo del algoritmo de hash
start = time.time()
l=len(line)
i=0 
while(l>0):
    #entrada = "password"
    entrada=line[i]
    E = basee64(entrada)
    Y = func_ascii(E)
    Z = hexadec(Y)
    t=len(Z)*4
    if(t<55):
        H = padding(Z)
    if(i==len(line)-1):
        l=0    
    i=i+1
    
#Termina algoritmo de hash (tiempo)
end = time.time()

print("Tiempo que demora algoritmo hash: ")
print(end - start)    
bases=64 #Base 64
largos=55 #Largo del string (hash)
#Calculo de entropia
entropias(bases,largos)
