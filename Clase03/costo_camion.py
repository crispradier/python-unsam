import csv

def costo_camion(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            header=next(rows)
            total=0
            for n,line in enumerate(rows, start=1):
                try:
                    cajones=float(line[1])
                    precio=float(line[2])
                    costo=cajones*precio
                    total+=costo
                except:
                    print(f'Fila {n}: No pude interpretar: {line}')
            return total
    except FileNotFoundError:
        print(f'Warning: {nombre_archivo} no es una ruta válida')


costo = costo_camion('../Data/missing.csv') 
print('Costo total:', costo)

