from utils import Convert

def RSA4(c, d, n):
    decrypt = pow(c,d,n)
    decrypted = Convert(decrypt)
    return decrypted
