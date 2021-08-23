import csv

def costo_camion(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            header=next(rows)
            total=0
            for n,line in enumerate(rows, start=1):
                record=dict(zip(header,line)) #dict usando zip para asociar encabezados con contenido
                
                try:
                    cajones=int(record['cajones'])
                    precio=float(record['precio'])
                    costo=cajones*precio
                    total+=costo
                except:
                    print(f'Fila {n}: No pude interpretar: {line}')
            return total
    except FileNotFoundError:
        print(f'Warning: {nombre_archivo} no es una ruta válida')


costo = costo_camion('../Data/fecha_camion.csv') 
print('Costo total:', costo)
#Costo total: 47671.15