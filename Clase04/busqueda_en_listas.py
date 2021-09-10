def buscar_u_elemento(lista, elemento):
    i=len(lista)-1
    posicion=-1
    while i>-1:
        if lista[i]==elemento:
            posicion=i
            break
        else:
            i-=1
    return posicion

# print(buscar_u_elemento([1,2,3,2,3,4],1))
# print(buscar_u_elemento([1,2,3,2,3,4],2))
# print(buscar_u_elemento([1,2,3,2,3,4],5))

def buscar_n_elemento(lista, elemento):
    i=0
    n=0
    while i<len(lista):
        if lista[i]==elemento:
            n+=1
        i+=1
    return n

# print(buscar_n_elemento([1,2,3,2,3,4],1))
# print(buscar_n_elemento([1,2,3,2,3,4],2))
# print(buscar_n_elemento([1,2,3,2,3,4],5))

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    assert lista!=[], 'La lista no debe estar vacía'
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = -9999999999 
    for e in lista: # Recorro la lista y voy guardando el mayor
        #assert e>=0, 'Todos los elementos deben ser positivos'
        if e>m:
            m=e
    return m

#print(maximo([])) AssertionError: La lista no debe estar vacía
print(maximo([-4,-5])) #AssertionError: Todos los elementos deben ser positivos
#print(maximo([10,2,6])) 10