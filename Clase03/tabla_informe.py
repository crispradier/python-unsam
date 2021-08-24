import csv

def leer_camion(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            header=next(rows)
            camion=[]
            for row in rows:
                item={}
                item['nombre']=row[0]
                item['cajones']=int(row[1])
                item['precio']=float(row[2])
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

def calcular_balance(camion,precios):
    valorCamion=0.0
    for s in camion:
            valorCamion+= s['cajones']*s['precio']
    valorVenta=0.0
    for s in camion:
        if s['nombre'] in precios:
            valorVenta+=precios[s['nombre']]*s['cajones']
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

def hacer_informe(camion,precios):
    informe=[]
    for item in camion:
        nombre=item['nombre']
        cajones=item['cajones']
        precio=item['precio']
        precio_venta=precios[nombre]
        cambio=precio_venta-precio
        tupla=(nombre,cajones,precio,cambio) 
        informe.append(tupla)
    return informe
    

camion = leer_camion('../Data/camion.csv') #cuidado, para que funcione hay que ejecutarlo desde Clase03
precios= leer_precios('../Data/precios.csv')
#calcular_balance(camion,precios)

#ejercicio 3.14
informe = hacer_informe(camion, precios)
#opcion con %
# for r in informe:
#     print('%10s %10d %10.2f %10.2f' % r)
#ejercicio 3.15 encabezados 
headers = ('Nombre','Cajones','Precio','Cambio')
nombre, cajones, precio, cambio = headers
print(f'{nombre:>10} {cajones:>10} {precio:>10} {cambio:>10}')
linea='-'*10
print(f'{linea} {linea} {linea} {linea}')
#opcion con f-strings
for nombre, cajones, precio, cambio in informe:
    precio_pesos=f'${precio:.2f}' #3.16
    print(f'{nombre:>10s} {cajones:>10d} {precio_pesos:>10} {cambio:>10.2f}')