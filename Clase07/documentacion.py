# Ejercicio 7.10: Funciones y documentación
#Para cada una de las siguientes funciones: * Pensá cuál es el contrato de la función.
#  * Agregale la documentación adecuada. * Comentá el código si te parece que aporta. 
# * Detectá si hay invariantes de ciclo y comentalo al final de la función

def valor_absoluto(n):
    ''' Calcula el módulo de n.
        pre: n es un número. 
        pos: devuelve el módulo de n
    '''
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    ''' 
    Suma los números pares de una lista l.
    pre: l debe ser una lista y contener números.
    pos: devuelve el valor de la suma
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
# inv: res contiene la suma de los números pares de l ya recorridos

def veces(a, b):
    ''' 
    Multiplica a por b.
    pre: a debe ser un número, b un número entero positivo.
    pos: devuelve a*b
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
#inv: res contiene la suma hasta el momento, nb la cantidad de ciclos que falta recorrer.

def collatz(n):
    ''' 
    calcula la cantidad de pasos que se tarda en llegar a 1 para el numero n, aplicando la conjetura de collatz.
    pre: n es un número entero positivo
    pos: devuelve la cantidad de pasos
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1   

    return res
# inv: res es la cantidad de pasos transcurridos