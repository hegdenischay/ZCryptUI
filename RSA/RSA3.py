from utils import egcd,modinv,Convert

def RSA3(c, n, e, p):
    q = n//p
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    decrypted = Convert(decrypt)
    return decrypted
