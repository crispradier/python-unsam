import random
import numpy as np

def medir_temp(n):
    temps=[]
    for x in range(n):
        medida=37.5+random.normalvariate(0,0.2)
        temps.append(medida)
    t=np.array(temps)
    np.save('Data/temperaturas', t)
    return temps

def resumen_temp(n):
    temps=medir_temp(n)
    maximo=max(temps)
    minimo=min(temps)
    promedio=sum(temps)/n
    temps.sort()
    if n%2==0:
        mediana=(temps[n//2]+temps[n//2-1])/2
    else:
        mediana=temps[(n-1)//2]
    resumen=(maximo, minimo, promedio, mediana)
    return resumen
    

#print(resumen_temp(101))
medir_temp(999)