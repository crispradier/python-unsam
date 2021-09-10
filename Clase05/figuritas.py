import random
import numpy as np

#Ejercicio 5.10: Crear
#Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío 
# con figus_total espacios para pegar figuritas.

def crear_album(figus_total):
    album=np.zeros(figus_total)
    return album
#mundial=crear_album(670)

#Ejercicio 5.11: Incompleto
#Implementá la función album_incompleto(A) que recibe un vector y devuelve True si el 
# álbum A no está completo y False si está completo.

def album_incompleto(A):
    return 0 in A
#print(album_incompleto(mundial))

#Ejercicio 5.12: Comprar
# Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas
#  que tiene el álbum (dado por el parámetro figus_total) y devuelva un número entero 
# aleatorio que representa la figurita que nos tocó.

def comprar_figu(figus_total):
    figu=random.randint(1,figus_total)
    return figu

#Ejercicio 5.13: Cantidad de compras
#Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), 
# genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron
#  comprar para completarlo.

def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    compras=0
    while album_incompleto(album):
        figurita=comprar_figu(figus_total)
        album[figurita-1]+=1
        compras+=1
    #print(album)
    return compras

#print(cuantas_figus(670))

#Ejercicio 5.14:
#Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardá en 
# una lista los resultados obtenidos en cada repetición. Con los resultados obtenidos estimá 
# cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas.

album_de_seis=[cuantas_figus(6) for i in range(1000)]
#print(np.mean(album_de_seis))

#Ejercicio 5.15:¶
#Escribí una función llamada experimento_figus(n_repeticiones, figus_total) que simule el llenado
#  de n_repeticiones álbums de figus_total figuritas y devuelva el número estimado de figuritas 
# que hay que comprar, en promedio, para completar el álbum.

def experimento_figus(n_repeticiones, figus_total):
    figus=[cuantas_figus(figus_total) for i in range(n_repeticiones)]
    return np.mean(figus)

#print(experimento_figus(100,670)) 
#da 4650.76, 4786.944

#Ejercicios con paquetes
#Ejercicio 5.16:
#Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 670. Tené en cuenta 
# que, como en la vida real, puede haber figuritas repetidas en un paquete.
paquete=[random.randint(1,670) for i in range(5)]

#Ejercicio 5.17:
#Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total)
# y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (lista) de figuritas al azar.

def comprar_paquete(figus_total, figus_paquete):
    paquete=[random.randint(1,figus_total) for i in range(figus_paquete)]
    return paquete

#Ejercicio 5.18:
#Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y la cantidad de 
# figus por paquete, genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.

def cuantos_paquetes(figus_total, figus_paquete):
    album=crear_album(figus_total)
    compras=0
    while album_incompleto(album):
        figuritas=comprar_paquete(figus_total, figus_paquete)
        compras+=1
        for figurita in figuritas:
            album[figurita-1]+=1
    return compras

#Ejercicio 5.19:
#Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 670, figus_paquete = 5. 
# Guarda los resultados obtenidos en una lista y calculá su promedio. Si te da la compu, hacelo con 1000 repeticiones.

album_de_670=[cuantos_paquetes(670,5) for i in range(100)]
# print(np.mean(album_de_670)) 
# con 100, da 946.85
# con 1000, da 952.431, 947.464

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()-1] = 1 #aca no funcionaba, agregué el -1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

# figus_total = 670
# figus_paquete = 5
# import matplotlib.pyplot as plt
# plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
# plt.xlabel("Cantidad de paquetes comprados.")
# plt.ylabel("Cantidad de figuritas pegadas.")
# plt.title("La curva de llenado se desacelera al final")
# plt.show()
#IndexError: index 670 is out of bounds for axis 0 with size 670, solucionado

# Ejercicio 5.20:
# Utilizando lo implementado en el ítem anterior, estimá la probabilidad de completar el álbum con 850 paquetes o menos.

def probabilidad_850(N):
    album=[cuantos_paquetes(670,5) for i in range(N)]
    E=0
    for n in album:
        if n<=850:
            E+=1
    return E/N
#print(probabilidad_850(100))

#25-27 (25 a 27%), con 1000 da 305, 30.5%

# #Ejercicio 5.21: Plotear el histograma
# #Usá un código similar al del Ejercicio 5.9 para hacer un histograma de la cantidad de paquetes que se compraron 
# # en cada experimento, ajustando la cantidad de bins para que el gráfico se vea lo mejor posible.
# import matplotlib.pyplot as plt
# plt.hist(album_de_670,bins=30)
# plt.show()

#Ejercicio 5.22:
#Utilizando lo implementado, estimá cuántos paquetes habría que comprar para tener una chance del 90% de completar el álbum.
def cuantos_paquetes_para(P, N):
    album=[cuantos_paquetes(670,5) for i in range(N)]
    E=int(P*N)
    album.sort()
    #print(album)
    return album[E] 
#print(cuantos_paquetes_para(0.9, 100))

#Ejercicio 5.23:
#Repetí suponiendo que no hay figuritas repetidas en un paquete. ¿Cuánto cambian las probabilidades?
def comprar_paquete_sin_repes(figus_total, figus_paquete):
    figus=[n for n in range(figus_total)]
    paquete=random.sample(figus,k=figus_paquete)
    return paquete

def cuantos_paquetes_sin_repes(figus_total, figus_paquete):
    album=crear_album(figus_total)
    compras=0
    while album_incompleto(album):
        figuritas=comprar_paquete_sin_repes(figus_total, figus_paquete)
        compras+=1
        for figurita in figuritas:
            album[figurita-1]+=1
    return compras

album_sin_repes=[cuantos_paquetes_sin_repes(670,5) for i in range(100)]
#print(np.mean(album_sin_repes)) 
#933.86

#Ejercicio 5.24: Cooperar vs competir
#Por último, suponé que cinco amigues se juntan y deciden compartir la compra de figuritas y el 
# llenado de sus cinco álbumes solidariamente. Calculá cuántos paquetes deberían comprar si deben
#  completar todos. Hacé 100 repeticiones y compará el resultado con la compra individual que 
# calculaste antes.
def cuantos_paquetes_solidario(figus_total, figus_paquete):
    album=crear_album(figus_total)
    compras=0
    while 0 in album or 1 in album or 2 in album or 3 in album or 4 in album:
        figuritas=comprar_paquete(figus_total, figus_paquete)
        compras+=1
        for figurita in figuritas:
            album[figurita-1]+=1
    print(album)
    return compras

#print(cuantos_paquetes_solidario(670, 5))
#1704, osea 341 por album