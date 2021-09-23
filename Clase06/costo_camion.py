#import csv
import informe_funciones as informe

def costo_camion(nombre_archivo):
    try:
        camion=informe.leer_camion(nombre_archivo)
        total=0
        for producto in camion:
            cajones=producto['cajones']
            precio=producto['precio']
            costo=cajones*precio
            total+=costo
        return total
    except FileNotFoundError:
        print(f'Warning: {nombre_archivo} no es una ruta válida')

costo = costo_camion('../Data/camion.csv') 
print('Costo total:', costo)

