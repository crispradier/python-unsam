# Ejercicio 11.2: Números triangulares
# Escribí una función que calcule recursivamente el n-ésimo número triangular 
# (es decir, el número 1 + 2 + 3 + ... + n).

def tri(n):
    #caso base
    if n==1:
        r=1
    #recursión
    else:
        r=n+tri(n-1)
    return r

# Ejercicio 11.3: Dígitos
# Escribí una función recursiva que reciba un número positivo, n, y devuelva la 
# cantidad de dígitos que tiene.

def digitos(n):
    if n//10==0:
        d=1
    else:
        d=1+digitos(n//10)
    return d

#print(digitos(99))

# Ejercicio 11.4: Potencias
# Escribí una función recursiva que reciba 2 enteros, n y b, y devuelva True si n es potencia de b.

def es_potencia(n,b):
    if n==1:
        r = True
    elif n%b!=0:
        r = False
    else:
        r=es_potencia(n//b,b)
    return r

#print(es_potencia(1, 3))

# Ejercicio 11.5: Subcadenas
# Escribí una funcion recursiva que reciba como parámetros dos cadenas a y b, y devuelva una lista con
# las posiciones en donde se encuentra b dentro de a.

def posiciones_de(a,b):
    if b not in a:
        r=[]
    else:
       i=a.index(b)
       a=a[:i]+'.'*len(b)+a[i+len(b):]
       r=[i]+(posiciones_de(a,b)) 
    return r

#print(posiciones_de('Un tete a tete con Tete', 'te'))

# Ejercicio 11.6: Paridad
# Escribí dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, usando solo que:
# 1 es impar.
# Un número mayor que uno es impar (resp. par) si su antecesor es par (resp. impar).

def impar(n):
    if n==1:
        r=True
    else:
        r=par(n-1)
    return r

def par(n):
    if n==1:
        r=False
    else:
        r=impar(n-1)
    return r

#print(impar(5))

# Ejercicio 11.7: Máximo
# Escribí una funcion recursiva que encuentre el mayor elemento de una lista (sin usar max()).