#Librerias 
import sys
import time
import math
import hashlib



def entropias(base,largo):
    print("")
    h=math.log(base, 2)*largo
    print("entropia:" )
    print(h)
    return h

def sha_256(entrada):
   # Codigo de SHA256  
    result = hashlib.sha256(entrada.encode())
    # Imprime el valor en hexadecimal
    print("Hexadecimal SHA256: ")
    print(result.hexdigest())
    print ("\r")
    return result  
 
def sha_1(entrada): 
    #Codigo de SHA1
    result = hashlib.sha1(entrada.encode())
    # Imprime el valor en hexadecimal
    print("Hexadecimal SHA1: ")
    print(result.hexdigest())
    return result

def MD_5(entrada):
    #Codigo de MD5
    result = hashlib.md5(entrada.encode())
# Imprime el valor en hexadecimal
    print("Hexadecimal MD5: ")
    print(result.hexdigest())
    return result

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
#Elegir el algoritmo de hash a utilizar
while(l>0):
    entrada=line[i]
    sha_1(entrada)
    #MD_5(entrada)
    #sha_256(entrada)
    if(i==len(line)-1):
        l=0 
    i=i+1
    
#Termina algoritmo de hash (tiempo)
end = time.time()
print("Tiempo en que tarda el algoritmo hash: ")
print(end - start)    
bases=36 #Bases: 36 en algoritmos MD5, SHA1 Y SHA256
largos=32    #largos: 40 en sha1, 32 en md5, 64 en sha256 
#Calculo de entropia
entropias(bases,largos)
