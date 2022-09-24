import random
import socket
import json

from RSA import RSA

x = ""
addr = ""
BASE_DIR = "/home/jwalvarez/Documents/taller_2_criptografia"


def create_server(host: str = "localhost", port: int = 8000):
    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mi_socket.bind((host, port))
    mi_socket.listen(5)

    while True:
        conexion, addr = mi_socket.accept()
        print("Conexión desde", addr)
        print("Esperando pk...")
        res = json.loads(conexion.recv(2048).decode("utf-8"))
        pk = (res[0], res[1])
        (n, e) = pk
        # print(pk)

        x = random.randint(0, n-1)
        print("x escogido.")

        rsaHacker = RSA()
        y = rsaHacker.Frsa(pk, x)
        y = str(y)

        print("enviando y...")
        conexion.send(bytes(y, "utf-8"))

        print("Conexión cerrada.", )

        with open(f'{BASE_DIR}/llave.txt', 'w') as f:
            f.write(f'{addr}\n')
            f.write(f'{x}')

        break

    mi_socket.close()


create_server()
