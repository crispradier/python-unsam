#import csv
import fileparse
import sys
import lote
from camion import Camion

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        camion_dict=fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types=[str, int, float])
        camion=[lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dict]
    return Camion(camion)

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = dict(fileparse.parse_csv(f, types=[str, float], has_headers=False))
    return precios

def calcular_balance(camion,precios):
    valorCamion=0.0
    for s in camion:
            valorCamion+= s.cajones*s.precio
    valorVenta=0.0
    for s in camion:
        if s.nombre in precios:
            valorVenta+=precios[s.nombre]*s.cajones
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
        nombre=item.nombre
        cajones=item.cajones
        precio=item.precio
        precio_venta=precios[nombre]
        cambio=precio_venta-precio
        tupla=(nombre,cajones,precio,cambio) 
        informe.append(tupla)
    return informe
    
# def imprimir_informe(informe):
#     headers = ('Nombre','Cajones','Precio','Cambio')
#     nombre, cajones, precio, cambio = headers
#     print(f'{nombre:>10} {cajones:>10} {precio:>10} {cambio:>10}')
#     linea='-'*10
#     print(f'{linea} {linea} {linea} {linea}')
#     for nombre, cajones, precio, cambio in informe:
#         precio_pesos=f'${precio:.2f}' #3.16
#         print(f'{nombre:>10s} {cajones:>10d} {precio_pesos:>10} {cambio:>10.2f}')

import formato_tabla

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion,archivo_precios, fmt = 'txt'):
    camion = leer_camion(archivo_camion) 
    precios= leer_precios(archivo_precios)
    informe = hacer_informe(camion, precios)
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)

def f_principal(parametros=sys.argv):
    camion = parametros[1]
    precios = parametros[2]
    if len(parametros)==4:
        fmt=parametros[3]
        informe_camion(camion, precios, fmt)
    else:
        informe_camion(camion, precios)

if __name__ == '__main__':
    f_principal()
    

#informe_camion('../Data/camion.csv','../Data/precios.csv')
#informe_camion('Data/camion2.csv', 'Data/precios.csv')
