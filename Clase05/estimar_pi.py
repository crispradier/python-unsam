import random
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def puntos(N):
    pts=[]
    for n in range(N):
        pts.append(generar_punto())
    return pts

def estimar_pi(N):
    M=0
    for n in range(N):
        x,y=generar_punto()
        if x**2 + y**2 < 1:
            M+=1
    pi=4*M/N
    return pi

print(estimar_pi(100000))