import random
from collections import Counter
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
# random.shuffle(naipes)
# print(naipes)
mano=random.sample(naipes,k=3)

def envido(mano):
    palos=[x[1] for x in mano]
    mas_comun=Counter(palos).most_common(1)
    if mas_comun[0][1]==2:
        palo=mas_comun[0][0]
        valores=[x[0] for x in mano if x[1]==palo]
        total=20
        for valor in valores:
            if valor<8:
                total+=valor
    else:
        total=0
    return total


def prob_envido(N, valor):
    envidos=[envido(random.sample(naipes,k=3)) for x in range (N)]
    validos=[x for x in envidos if x==valor]
    prob=len(validos)/N
    return prob   

print(prob_envido(10000,31)) #0.025
print(prob_envido(10000,32)) #0.012
print(prob_envido(10000,33)) #0.01