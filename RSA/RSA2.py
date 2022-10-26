from utils import modinv, Convert

def RSA2(c, p, q, e):
    n = p*q
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    decrypted = Convert(decrypt)
    return decrypted
