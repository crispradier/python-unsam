import csv
import sys

def costo_camion(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            header=next(rows)
            total=0
            for line in rows:
                try:
                    cajones=float(line[1])
                    precio=float(line[2])
                    costo=cajones*precio
                    total+=costo
                except:
                    pass
            return total
    except:
        print(f'Warning: {nombre_archivo} no es una ruta válida')


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

#python camion_commandline.py ../Data/missing.csv
#Costo total: 30381.15

# D:\unsam\Ejercicios\python-unsam\ejercicios_python\Clase02> python camion_commandline.py ../Data/camion.csv 
# Costo total: 47671.15