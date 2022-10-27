from utils import *
from factorizations.factordb import *

def factordb(n):
    f = FactorDB(n)
    f.connect()
    return f.get_factor_list()

def RSA1(c, n, e):
    factordb = factordb(n)
    q = factordb[0]
    p = factordb[1]
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    decrypted = Convert(decrypt)
    return decrypted
