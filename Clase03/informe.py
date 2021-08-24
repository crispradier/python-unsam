#nueva versión usando zip(), se corre desde clase03

import csv

def leer_camion(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            header=next(rows)
            camion=[]
            for row in rows:
                item=dict(zip(header,row))
                item['cajones']=int(item['cajones'])
                item['precio']=float(item['precio'])
                camion.append(item)
            return camion
    except:
        print(f'Warning: {nombre_archivo} no es una ruta válida')

def leer_precios(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            precios={}
            for row in rows:
                try:
                    precios[row[0]] = float(row[1])
                except IndexError:
                    pass
            return precios
    except:
        print(f'Warning: {nombre_archivo} no es una ruta válida')


camion = leer_camion('../Data/fecha_camion.csv') 
precios= leer_precios('../Data/precios.csv')

valorCamion=0.0
for s in camion:
        valorCamion+= (s['cajones'])*(s['precio'])

valorVenta=0.0
for s in camion:
    if s['nombre'] in precios:
        valorVenta+=precios[s['nombre']]*(s['cajones'])
    else:
        print('no está en la lista de precios')

diferencia=valorVenta-valorCamion

print(f'El camión costó {valorCamion}, con la venta se recaudó {valorVenta} y la diferencia fue de {diferencia:.2f}.')
if diferencia>0:
    print('Hubo ganancia.')
elif diferencia==0:
    print('El balance es cero.')
else:
    print('Hubo pérdida.')

from collections import Counter
tenencias=Counter()
for s in camion:
    tenencias[s['nombre']] += (s['cajones'])


camion2 = leer_camion('../Data/camion2.csv')
tenencias2 = Counter()
for s in camion2:
    tenencias2[s['nombre']] += s['cajones']

combinada = tenencias + tenencias2
print(combinada)