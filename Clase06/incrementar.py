def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

#print(incrementar([0,0,0,1,0]))

def listar_secuencias(n):
    secuencias=[[0]*n]
    sec=[0]*n
    for i in range(2**n-1):
        sig=incrementar(sec)
        secuencias.append(sig[:]) 
        sec=sig  
    return secuencias
#print(listar_secuencias(15))
# 2**n, es exponencial

