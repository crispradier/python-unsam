# Este archivo contiene todos los ejercicios de la parte 3.7 Arbolado porteño
# En cada ejercicio está la función pedida, y después la sentencia print correspondiente y los resultados comentados 

import csv
from pprint import pprint

# Ejercicio 3.18: Lectura de los árboles de un parque
def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        lineas=csv.reader(f)
        headers=next(lineas)
        arboles=[]
        for linea in lineas:
            if linea[10]==parque:
                arbol=dict(zip(headers,linea))
                arbol['altura_tot']=float(arbol['altura_tot'])
                arbol['inclinacio']=float(arbol['inclinacio'])
                arboles.append(arbol)
        return arboles
arboles=leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
#pprint(arboles)



# Ejercicio 3.19: Determinar las especies en un parque
def especies(lista_arboles):
    lista_especies=[]
    for arbol in lista_arboles:
        especie=arbol['nombre_com']
        lista_especies.append(especie)
    conjunto=set(lista_especies)
    return conjunto

#print(especies(arboles))



# Ejercicio 3.20: Contar ejemplares por especie
from collections import Counter

def contar_ejemplares(lista_arboles):
    ejemplares=Counter()
    for arbol in lista_arboles:
        ejemplares[arbol['nombre_com']]+=1
    return ejemplares

def mas_ejemplares(nombre_archivo, parque, cantidad):
    arboles=leer_parque(nombre_archivo, parque)
    mas_comunes=contar_ejemplares(arboles).most_common(cantidad)
    return mas_comunes

#print(contar_ejemplares(arboles))

# print(mas_ejemplares('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ',5))
# [('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]

# print(mas_ejemplares('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS',5))
# [('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]

# print(mas_ejemplares('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO',5))
# [('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]



# Ejercicio 3.21: Alturas de una especie en una lista
def obtener_alturas(lista_arboles, especie):
    alturas=[]
    for arbol in lista_arboles:
        if arbol['nombre_com']==especie:
            alturas.append(arbol['altura_tot'])
    return alturas
    # usando en vez: return alturas, max(alturas), sum(alturas)/len(alturas)
    # devuelve las alturas, maximo y promedio
    #lo saqué para que funcione el ejercicio de los extras

# print(obtener_alturas(arboles, 'Jacarandá'))
# GENERAL PAZ:
#([10.0, 10.0, 10.0, 13.0, 10.0, 14.0, 13.0, 8.0, 8.0, 13.0, 10.0, 10.0, 10.0, 7.0, 8.0, 14.0, 16.0, 6.0, 8.0, 6.0], 16.0, 10.2)
# max = 16.0
# prom = 10.2


# Ejercicio 3.22: Inclinaciones por especie de una lista
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones=[]
    for arbol in lista_arboles:
        if arbol['nombre_com']==especie:
            inclinaciones.append(arbol['inclinacio'])
    return inclinaciones

#print(obtener_inclinaciones(arboles, 'Jacarandá'))



# Ejercicio 3.23: Especie con el ejemplar más inclinado
def especimen_mas_inclinado(lista_arboles):
    conjunto=especies(lista_arboles)
    mayor=0
    for especie in conjunto:
        inclinaciones=obtener_inclinaciones(lista_arboles, especie)
        maximo=max(inclinaciones)
        if maximo>mayor:
            mayor=maximo
            especie_mas_inclinada=especie
    return especie_mas_inclinada, mayor

# arboles=leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
# print(especimen_mas_inclinado(arboles))
# ('Falso Guayabo (Guayaba del Brasil)', 80.0)
# arboles=leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
# print(especimen_mas_inclinado(arboles))
# ('Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert)', 70.0)
# arboles=leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
# print(especimen_mas_inclinado(arboles))
# ('Jacarandá', 30.0)

# Ejercicio 3.24: Especie más inclinada en promedio
def especie_promedio_mas_inclinada(lista_arboles):
    conjunto=especies(lista_arboles)
    mayor=0
    for especie in conjunto:
        inclinaciones=obtener_inclinaciones(lista_arboles, especie)
        promedio=sum(inclinaciones)/len(inclinaciones)
        if promedio>mayor:
            mayor=promedio
            especie_promedio_mas_inclinada=especie
    return especie_promedio_mas_inclinada, mayor

# arboles=leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
# print(especie_promedio_mas_inclinada(arboles))
# ('Álamo plateado', 25.0)

# Preguntas extras: ¿Qué habría que cambiar para obtener la especie con un ejemplar más inclinado 
# de toda la ciudad y no solo de un parque? ¿Podrías dar la latitud y longitud de ese ejemplar? 
# ¿Y dónde se encuentra (lat,lon) el ejemplar más alto? ¿De qué especie es?

def leer_arbolado(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        lineas=csv.reader(f)
        headers=next(lineas)
        arboles=[]
        for linea in lineas:
            arbol=dict(zip(headers,linea))
            arbol['altura_tot']=float(arbol['altura_tot'])
            arbol['inclinacio']=float(arbol['inclinacio'])
            arboles.append(arbol)
        return arboles

arboles=leer_arbolado('../Data/arbolado-en-espacios-verdes.csv')

def id_especimen_mas_inclinado(lista_arboles):
    conjunto=especies(lista_arboles)
    mayor=0
    id=0
    lat=0
    long=0
    for especie in conjunto:
        inclinaciones=obtener_inclinaciones(lista_arboles, especie)
        maximo=max(inclinaciones)
        if maximo>mayor:
            mayor=maximo
            especie_mas_inclinada=especie
    for arbol in lista_arboles:
        if arbol['nombre_com']==especie_mas_inclinada and arbol['inclinacio']==mayor:
            id=arbol['id_arbol']
            lat=arbol['lat']
            long=arbol['long']
    resultado=f'El arbol más inclinado es un {especie_mas_inclinada} de id {id}, ubicado en {lat}, {long}, y su inclinación es {mayor} grados'
    return resultado

#print(id_especimen_mas_inclinado(arboles))
#El arbol más inclinado es un Cedro del Himalaya de id 50787, ubicado en -34.5495758129, -58.437764978000004, y su inclinación es 90.0 grados
# en realidad hay varios arboles inclinados a 90 grados, reporta solo uno

def id_especimen_mas_alto(lista_arboles):
    conjunto=especies(lista_arboles)
    mayor=0
    id=0
    lat=0
    long=0
    for especie in conjunto:
        alturas=obtener_alturas(lista_arboles, especie)
        maximo=max(alturas)
        if maximo>mayor:
            mayor=maximo
            especie_mas_inclinada=especie
    for arbol in lista_arboles:
        if arbol['nombre_com']==especie_mas_inclinada and arbol['altura_tot']==mayor:
            id=arbol['id_arbol']
            lat=arbol['lat']
            long=arbol['long']
    resultado=f'El arbol más alto es un {especie_mas_inclinada} de id {id}, ubicado en {lat}, {long}, y su altura es {mayor}'
    return resultado

#print(id_especimen_mas_alto(arboles))
#El arbol más alto es un Rosa de Siria de id 4232, ubicado en -34.5818308351, -58.398926961099995, y su altura es 54.0  