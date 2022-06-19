# Laboratorio 3
# Hito 1
1) Objetivo (caso de uso):

Se busca generar integridad en los datos y confidencialidad en las contraseñas al momento de ser ingresadas por el usuario cuando realiza un inicio de sesión y estas almacenarse posteriormente en la base de datos. Dichas contraseñas se almacenan hasheadas en la tabla de base de datos para poder proteger dichos datos de acceso frente a un robo de los datos por ejemplo. Además, en la base de datos se trabaja de mejor manera con tablas de hash para poder no solo garantizar mayor seguridad sino también trabajar de mejor manera las búsquedas. Por lo que se debe implementar un algoritmo que garantice que dichas contraseñas estén hasheadas y así poder permitir integridad y confidencialidad en los datos almacenados en la base de la página web.

2) Algoritmo:

En primer lugar se efectua la idea general del funcionamiento del algoritmo el cual consiste en lo siguiente:

1. Primero transforma a base 64 (base utilizada en el algoritmo) los valores de entrada.
2. luego se transforma a ASCII.
3. Posteriormente se pasa a hexadecimal.
4. Después se aplica un padding en caso de ser necesario (en caso de ser necesario para completar el hash de 55 caracteres, este padding se rellena con “x”).
5. Finalmente se obtiene el valor de hash (salida).

Nota: Todo esto se puede ver de mejor forma en el diagrama (archivo adjunto).

# Hito 2
En este caso se efectua el codigo del algoritmo con todos los puntos mencionados anteriormente, ademas de cumplir con lo del gremio de dueños de sitios webs vulnerados.

Nota: Todo ello se puede ver en la parte de codigos (archivo adjunto).


# Hito 3
Se efectua comparaciones entre la funcion hash realizada y otras ya imnplementadas como por ejemplo, MD5, SHA1, SHA256, ademas de efectuar pruebas de archivos de texto (1 entrada de texto, 10 entradas de texto, 20 entradas de texto, 50 entradas de texto).

Nota: Todo esto se puede ver de mejor manera en el archivo adjunto "Hito 3.pdf" y en la parte de codigos.

Nota: Se sacaron del diccionario público Rockyou.txt credenciales para poder efectuar las pruebas de texto.
