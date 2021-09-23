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
#print(maximo([-4,-5])) #AssertionError: Todos los elementos deben ser positivos
#print(maximo([10,2,6])) 10

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    lista.sort()
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z > e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

#print(busqueda_lineal([1, 4, 54, 3, 0, -1], 44))
#print(busqueda_lineal([1, 4, 54, 3, 0, -1], 3))

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos