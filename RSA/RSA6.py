from utils import Convert
import gmpy2
import binascii

def RSA6(c, e):
    m = gmpy2.iroot(c,e)[0]
    assert pow(m,e) == c
    decrypted = Convert(m)
    return decrypted
