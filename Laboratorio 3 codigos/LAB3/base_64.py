import base64

entrada = "hola"
print("Entrada: " + entrada)
bs64= base64.b64encode(entrada.encode('ascii'))
print("codigo en base64: " + str(bs64))

