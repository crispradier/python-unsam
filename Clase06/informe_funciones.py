import csv
import fileparse

def leer_camion(nombre_archivo):
    camion=fileparse.parse_csv(nombre_archivo, types=[str, int, float])
    return camion

def leer_precios(nombre_archivo):
    precios = dict(fileparse.parse_csv(nombre_archivo, types=[str, float], has_headers=False))
    return precios

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
    
def imprimir_informe(informe):
    headers = ('Nombre','Cajones','Precio','Cambio')
    nombre, cajones, precio, cambio = headers
    print(f'{nombre:>10} {cajones:>10} {precio:>10} {cambio:>10}')
    linea='-'*10
    print(f'{linea} {linea} {linea} {linea}')
    for nombre, cajones, precio, cambio in informe:
        precio_pesos=f'${precio:.2f}' #3.16
        print(f'{nombre:>10s} {cajones:>10d} {precio_pesos:>10} {cambio:>10.2f}')

def informe_camion(archivo_camion,archivo_precios):
    camion = leer_camion(archivo_camion) 
    precios= leer_precios(archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

#informe_camion('../Data/camion.csv','../Data/precios.csv')
#informe_camion('Data/camion2.csv', 'Data/precios.csv')