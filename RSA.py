from Crypto.Util import number
# import gensafeprime
import random


class RSA:
    # k y e son primos relativos, gcd(k,e)=1
    def Grsa(self, l, e):
        p = number.getPrime(l)  # Generar un primo con l bits

        while number.GCD(p-1, e) != 1:
            p = number.getPrime(l)
        # dos números a, b se dicen primos relativos si y solo si GCD(a, b)=1
        # print('p:=', p)
        q = number.getPrime(l)
        while number.GCD(q-1, e) != 1 or p == q:
            q = number.getPrime(l)

        # print('q:=', q)

        # p y q son primos de l bits tal que p!=q y GCD(p-1,e)=1 y GCD(q-1,e)=1

        phi = (p-1)*(q-1)  # phi(n)
        d = number.inverse(e, phi)  # . e*d = 1 mod phi,  e*d = c*phi +1
        # print('e=', e)
        # print('d=', d)
        n = p*q
        # print('n=', n)
        pk = (n, e)
        sk = (n, d)
        # print('(e*d) mod (p-1)*(q-1)=', (e*d) % phi)
        return sk, pk

    def Frsa(self, pk, x):  # x \in Zn= {0,1,2,3,4,...,n-1}
        (n, e) = pk
        y = pow(x, e, n)  # x^e mod n // x**e  % n
        return y
    # gcd(x,n)=1.  x está en el grupo Zn* tiene orden phi

    def Irsa(self, sk, y):
        (n, d) = sk
        # y^d mod n =x ---> x^(ed) mod n ---> x^(q*phi +1) mod n ---> x^(q*phi)*x mod n---> 1*x mod n
        x = pow(y, d, n)
        return x
