'''
En tu directorio de trabajo de esta clase, escribí un programa llamado esfera.py que le pida al usuario 
que ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma. 
Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.

Finalmente, ejecutá el programa desde la línea de comandos para responder ¿cuál es el volumen de 
una esfera de radio 6? Debería darte 904.7786842338603.
'''
import math

def esfera(r):
    vol=(4/3)*math.pi*r**3
    print(vol)

radio=float(input('Ingresá el radio de la esfera:\n'))
esfera(radio)

'''
Ingresá el radio de la esfera:
6
904.7786842338603
'''