# taller_2_criptografia

## Paso a paso del ataque:
1. En primer lugar, se debe establecer la ruta base (dentro de ransomware.py) la cual simulará la estructura de directorios del sistema operativo de la víctima. 

2. Ejecutar ```python hacker.py``` para levantar el servidor del lado del atacante, ya que este debe estar a la escucha de las conexiones que se hagan hacia él. 

3. Una vez la victima tenga el ransomware en su máquina, se procede a ejecutar: ```python ransomware.py```

    Advertencia: En este punto se debe definir bien la ruta BASE_DIR donde se simulará 	el directorio del sistema de la víctima. En nuestro caso particular es:  


    ```
    BASE_DIR = "/home/jwalvarez/Documents/taller_2_criptografia/PC" 
    ```

4. En este paso, el ransomware establecerá una conexión con el hacker, en donde se intercambiará un secreto y así poder generar la llave de encriptación. 

5. Luego, el hacker escogerá una x, la cual cifrará y enviará por medio de la conexión a la víctima, es decir, se envía y, donde 
    ```
    y ⟵ F(pk, x) 
    ```

6. El ransomware descifrará la y recibida, obteniendo x de esta forma: 
    ```
    x ⟵ I(sk, y), x se usará para generar una key  

    key ⟵ getKey(x)

    key ⟵ getKeyx
    ```

7. Finalmente, se recorren todos los archivos dentro de la ruta BASE_DIR y se proceden a encriptarlos con la key generada, creando así el archivo de INSTRUCCIONES.txt que tendrá la lista de archivos encriptados y el paso a paso a seguir para rescatar los archivos. 


## Pasos para desencriptar los archivos:
Una vez se tengan los archivos encriptados y se haya pagado el rescate, el proceso de encriptación es el siguiente: 

1. Se debe establecer la misma ruta definida en ```BASE_DIR``` y pegar la llave enviada por el atacante. 

2. Ejecutar ```python desencriptar_archivos.py```