import random

def tirar(n):
    tirada=[]
    for i in range(n):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    valor=tirada[0]==tirada[1] and tirada[0]==tirada[2] and tirada[0]==tirada[3] and tirada[0]==tirada[4]
    return valor

# N=1000000
# G = sum([es_generala(tirar(5)) for i in range(N)])
# prob = G/N
# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
# Tiré 1000000 veces, de las cuales 737 saqué generala servida.
# Podemos estimar la probabilidad de sacar generala servida mediante 0.000737.

from collections import Counter

def generala():
    tirada1=tirar(5)
    mas_comun=Counter(tirada1).most_common(1)
    numero, repeticiones=mas_comun[0]
    final=[numero for x in range(repeticiones)]
    if repeticiones<5:
        tirada2=tirar(5-repeticiones)
        for n in tirada2:
            if n==numero:
                final.append(n)
                repeticiones+=1
    if repeticiones<5:
        tirada3=tirar(5-repeticiones)
        for n in tirada3:
            final.append(n)
    return final           


def prob_generala(N):
    G=sum([es_generala(generala()) for x in range(N)])
    prob=G/N
    return prob

print(prob_generala(100000)) #0.04588 eligiendo siempre un dado en la primera tirada

def generala_tirando_de_nuevo():
    tirada1=tirar(5)
    mas_comun=Counter(tirada1).most_common(1)
    numero, repeticiones=mas_comun[0]
    if repeticiones>1:
        final=[numero for x in range(repeticiones)]
        if repeticiones<5:
            tirada2=tirar(5-repeticiones)
            for n in tirada2:
                if n==numero:
                    final.append(n)
                    repeticiones+=1
        if repeticiones<5:
            tirada3=tirar(5-repeticiones)
            for n in tirada3:
                final.append(n)
    else:
        tirada2=tirar(5)
        mas_comun=Counter(tirada2).most_common(1)
        numero, repeticiones=mas_comun[0]
        final=[numero for x in range(repeticiones)]
        if repeticiones<5:
            tirada3=tirar(5-repeticiones)
            for n in tirada3:
                final.append(n)
                    
    return final  

def prob_generala_de_nuevo(N):
    G=sum([es_generala(generala_tirando_de_nuevo()) for x in range(N)])
    prob=G/N
    return prob

print(prob_generala_de_nuevo(100000)) #da muy similar