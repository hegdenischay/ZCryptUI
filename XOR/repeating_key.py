from pwn import xor
import binascii

def repeating_key(c,key):
    flag = xor(c,key)
    return flag
