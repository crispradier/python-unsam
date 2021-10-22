#import csv
import sys
import informe_final as informe
from camion import Camion

def costo_camion(nombre_archivo):
    try:
        camion=informe.leer_camion(nombre_archivo)
        total=camion.precio_total()

        return total
    except FileNotFoundError:
        print(f'Warning: {nombre_archivo} no es una ruta válida')


def f_principal(parametros=sys.argv):
    camion = parametros[1]
    return costo_camion(camion)

if __name__=="__main__":
    costo=f_principal()
    print('Costo total:', costo)

