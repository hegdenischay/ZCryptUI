from pwn import xor
def bruteforce(ct):
    flag = []
    for i in range(255):
        flag.append(xor(ct,i))
    out = ""
    for i in range(len(flag)):
        out += f"XOR Key: {i}, XORed output: {flag[i]}\n"
    return out
