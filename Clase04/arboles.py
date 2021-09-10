# Ejercicio 4.15: Lectura de todos los árboles
# Basándote en la función leer_parque(nombre_archivo, parque) del Ejercicio 3.18, escribí otra 
# leer_arboles(nombre_archivo) que lea el archivo indicado y devuelva una lista de diccionarios 
# con la información de todos los árboles en el archivo. La función debe devolver una lista 
# conteniendo un diccionario por cada árbol con todos los datos.
# Vamos a llamar arboleda a esta lista.
import csv
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        lineas=csv.reader(f)
        headers=next(lineas)
        arboleda=[]
        for linea in lineas:
            arbol=dict(zip(headers,linea))
            arbol['altura_tot']=float(arbol['altura_tot'])
            arbol['inclinacio']=float(arbol['inclinacio'])
            arboleda.append(arbol)
        return arboleda
arboleda=leer_arboles('Data/arbolado-en-espacios-verdes.csv') #debe ejecutarse desde ejercicios_python
# cuidado! tarda bastante en imprimir todo 
# print(arboleda)

# Ejercicio 4.16: Lista de altos de Jacarandá
# Usando comprensión de listas y la variable arboleda podés por ejemplo armar la lista de la altura de los árboles.
# Usá los filtros (recordá la Sección 4.3) para armar la lista de alturas de los Jacarandás solamente.

H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
#print(H)

# Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
# En el ejercicio anterior usaste una sola linea para seleccionar las alturas de los Jacarandás en parques porteños.
# Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto 
# sino también el diámetro de cada Jacarandá en la lista.

HyD=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
#print(HyD)

# Ejercicio 4.18: Diccionario con medidas

def medidas_de_especies(especies,arboleda):
    diccionario={}
    for especie in especies:
        medidas=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
        diccionario[especie]=medidas
        #print(especie, len(diccionario[especie]))
        #esta ultima linea esta para ver si funcionó bien el código
    return diccionario
    

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
dict_medidas= medidas_de_especies(especies,arboleda)


# con comprension:
diccionario={especie:[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie] for especie in especies}
# print(diccionario)

#Ejercicio 5.25: Histograma de altos de Jacarandás
#Usando tu trabajo en el Ejercicio 4.16, generá un histograma con las alturas de los Jacarandás en el dataset.
import matplotlib.pyplot as plt
# plt.hist(H,bins=27) #H es la lista de altos de jacarandá
# plt.show()

#Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
#Escribí una función scatter_hd(lista_de_pares) que a partir de una lista de pares como la que generaste en el Ejercicio 4.17 
# genere un scatterplot para visualizar la relación entre altura y diámetro de los Jacarandás del dataset.
HyD=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
import numpy as np
def scatter_hd(lista_de_pares):
    lista=np.array(lista_de_pares)
    d=lista[0:,1]
    h=lista[0:,0]
    # sin usar numpy:
    # colors=[]
    # for arbol in lista_de_pares:
    #     d.append(arbol[1])
    #     h.append(arbol[0])
    #     colors.append(arbol[0])
    plt.scatter(d,h, alpha=0.4) # y agregar c=colors aca
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()
#scatter_hd(HyD)


# Ejercicio 5.27: Scatterplot para diferentes especies
# Ahora vamos a usar la función medidas_de_especies() definida en el Ejercicio 4.18.

# Comenzando con éste código, hacé tres gráficos como en el ejercicio anterior, uno por cada especie.

def scatter_especies_hd(especies):
    medidas = medidas_de_especies(especies, arboleda)
    d=[]
    h=[]
    colors=[]
    for especie in especies:
        lista_de_pares=medidas[especie]
        for arbol in lista_de_pares:
            d.append(arbol[1])
            h.append(arbol[0])
            colors.append(especies.index(especie))
    plt.scatter(d,h, c=colors, alpha=0.4)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.xlim(0,100) 
    plt.ylim(0,52) 
    plt.title(f"Relación diámetro-alto para {especies}")
    plt.show()

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
#scatter_especies_hd(especies)
