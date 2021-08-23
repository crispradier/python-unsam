#%%
#Ejercicio 3.1. Semántica, Función tiene_a()
#Comentario: El error era de tipo semántico y estaba ubicado en el if y el else. 
# Como en ambas condiciones había un return, el ciclo se cortaba siempre despues 
# de la primera iteracion, por lo tanto no evaluaba si la expresion "tiene a", 
# sino si el primer caracter era una a.
# Lo corregí cambiando la condición else, para que avance a lo largo del string,
# y moviendo el return False hacia afuera del ciclo while, para que la respuesta 
# sea False solo si el programa no encontró ninguna a antes
# A continuación va el código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2: Sintaxis
# Comentario: Los errores eran de tipo sintáctico y estaban ubicados en 
# el def, el while, el if y al final en el return.
# Los corregí agregando los : al definir la expresión, después del while y del if
# (también un = extra en el if), y cambiando Falso por False.
# A continuación va el código corregido:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
# %%
#Ejercicio 3.3: Tipos
# Comentario: Daba un error de tiempo de ejecucion, TypeError, que se generaba porque
# la funcion no estaba preparada para manejar inputs de tipo int. 
# Lo corregí convirtiendo el input, expresion, a str antes de empezar a trabajar con él.
# A continuación va el código corregido:

def tiene_uno(expresion):
    expresion=str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
# %%
#Ejercicio 3.4: Alcances
# Comentario: En este caso el resultado no es el esperado porque 
# la función definida no devuelve ningún resultado.
# Lo corregí agregando un return al final de la función.
# A continuación va el código corregido:

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

# %%
#Ejercicio 3.5: Pisando memoria
# Comentario: En este caso el resultado no es el esperado porque el diccionario 
# registro se sobreescribe con cada iteración, y, al estar asociado a camion (camion contiene 
# multiples registros, que son todos el mismo), al modificarse registro se modifica tambien camion.
# Lo corregí inicializando registro dentro del for en vez de al principio de la función.
# A continuación va el código corregido:
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

#%%

# %%
