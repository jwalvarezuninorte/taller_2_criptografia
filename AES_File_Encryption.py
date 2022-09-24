import os
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad


def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename+".enc"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:  # rb means read in binary
        with open(outputFile, 'wb') as outfile:  # wb means write in the binary mode
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk = pad(chunk, 16)

                outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename[:-4]

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(filesize)


def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()


def Main():
    choice = input("Te gustaría Cifrar (C) o descifrar (D)")

    if choice == 'C':
        filename = input("Ruta de archivo a cifrar : ")
        password = input("Contraseña: ")
        encrypt(getKey(password), filename)
        print('Hecho.')
    elif choice == 'D':
        filename = input("Ruta de archivo a descifrar : ")
        password = input("Contraseña: ")
        decrypt(getKey(password), filename)
        print("Hecho.")

    else:
        print("Ninguna opción ha sido seleccionada.")


# Main()
