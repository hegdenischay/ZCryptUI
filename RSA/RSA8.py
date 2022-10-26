from utils import *

def fermat_factors(n):
    assert n % 2 != 0
    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
    return a + gmpy2.isqrt(b2), a - gmpy2.isqrt(b2)

    c = int(input("==> c = "))
    n = int(input("==> n = "))
    e = int(input("==> e = "))

def RSA8(c, n, e):
    p, q = fermat_factors(n)
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    decrypted = convert(decrypt)
    return decrypted
