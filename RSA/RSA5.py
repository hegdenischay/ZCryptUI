from utils import Convert
import functools
import gmpy

def crt(n, a):
   sum = 0
   prod = functools.reduce(lambda a, b: a*b, n)
   for i,j in zip(n,a):
       p = prod // i
       sum += j * gmpy.invert(p,i) * p
   return sum % prod

def RSA5(c1, c2, c3, n1, n2, n3):
    N = [n1, n2, n3]
    C = [c1, c2, c3]
    e = len(N)
    a = crt(N,C)
    for n,c in zip(N, C):
        assert a % n == c
    m = gmpy.root(a,e)[0]
    decrypted = Convert(m)
    return decrypted
