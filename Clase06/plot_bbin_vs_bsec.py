import random
import matplotlib.pyplot as plt
import numpy as np

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria_(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Ademas devuelve la cantidad de comparaciones
    '''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps=0
    while izq <= der:
        comps+=1
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, comps

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def graficar_bbin_vs_bseq(m, k):
    largos = np.arange(256) + 1 
    comps_promedio_sec = np.zeros(256) 
    comps_promedio_bin = np.zeros(256)
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) 
        comps_promedio_sec[i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)
       
    plt.plot(largos,comps_promedio_sec,label = 'Búsqueda Secuencial')
    plt.plot(largos,comps_promedio_bin,label = 'Búsqueda Binaria')
    plt.ylim(0, 50)
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Comparación entre dos algoritmos de búsqueda, de complejidades lineal y logarítmica")
    plt.legend()
    plt.show()

# if __name__=="__main__":
#     m = 10000
#     k = 1000
#     graficar_bbin_vs_bseq(m,k)
    # largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    # comps_promedio_sec = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    # comps_promedio_bin = np.zeros(256)
    

    # for i, n in enumerate(largos):
    #     lista = generar_lista(n, m) # genero lista de largo n
    #     comps_promedio_sec[i] = experimento_secuencial_promedio(lista, m, k)
    #     comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)
    
    # # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    # plt.plot(largos,comps_promedio_sec,label = 'Búsqueda Secuencial')
    # plt.plot(largos,comps_promedio_bin,label = 'Búsqueda Binaria')
    # plt.ylim(0, 50)
    # plt.xlabel("Largo de la lista")
    # plt.ylabel("Cantidad de comparaciones")
    # plt.title("Complejidad de la Búsqueda")
    # plt.legend()
    # plt.show()


