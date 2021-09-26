import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()


def plot_randomwalk(n):
    pasos = 100000
    lejos = 0
    cerca = 1000
    plt.subplot(2, 1, 1)
    for i in range(n):
        y=randomwalk(pasos)
        plt.plot(y)
        if abs(max(y))>lejos or abs(min(y))>lejos:
            a=y.copy()
            lejos=max(abs(max(y)),abs(min(y)))
        if abs(max(y))<cerca and abs(min(y))<cerca:
            b=y.copy()
            cerca=max(abs(max(y)),abs(min(y)))
    plt.xlabel("tiempo")
    plt.ylabel("distancia al origen")
    plt.title("12 caminatas al azar")
    
    
    plt.subplot(2, 2, 3)
    plt.plot(a)
    plt.ylim(min(min(a), min(b))-50, max(max(a), max(b))+50)
    plt.xlabel("tiempo")
    plt.ylabel("distancia al origen")
    plt.title("caminata que más se aleja")
    
    
    plt.subplot(2, 2, 4)
    plt.plot(b)
    plt.ylim(min(min(a), min(b))-50, max(max(a), max(b))+50)
    plt.xlabel("tiempo")
    plt.ylabel("distancia al origen")
    plt.title("caminata que menos se aleja")
    
    
    plt.show()
    
    
if __name__ == "__main__":  
    plot_randomwalk(12)
    