import base64
import sys


def basee64(entrada):
    #entrada = "hola"
    print("Entrada: " + entrada)
    bs64= base64.b64encode(entrada.encode('ascii'))
    print("codigo en base64: " + str(bs64))
    return entrada

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
    ceross=""
    print(ceross.ljust(55-tamaño,"0"))



def hexadec(entrada):
    #entrada= 'Sample String'.encode('utf-8')
    #decimal = int(input("Enter a number: "))
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

#Lectura archivos
f = open('credenciales.txt')
line=f.readlines()
#print(line[0])


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
    #if(t<55):
    if(i==len(line)-1):
        l=0    
    i=i+1