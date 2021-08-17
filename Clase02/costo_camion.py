import csv

def costo_camion(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            header=next(rows)
            total=0
            for line in rows:
                cajones=float(line[1])
                precio=float(line[2])
                costo=cajones*precio
                total+=costo
            return total
    except:
        print(f'Warning: {nombre_archivo} no es una ruta válida')


costo = costo_camion('../Data/camion.csv') #cuidado, para que funcione hay que ejecutarlo desde Clase02
print('Costo total:', costo)
#Costo total: 47671.15


'''
sin csv
def costo_camion(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            header=next(f)
            total=0
            for line in f:
                linea=line.split(',')
                cajones=float(linea[1])
                precio=float(linea[2])
                costo=cajones*precio
                total+=costo
            return total
    except:
        print(f'Warning: {nombre_archivo} no es una ruta válida')
'''