import csv
f = open('Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
select = ['nombre', 'cajones', 'precio']
indices = [headers.index(ncolumna) for ncolumna in select]
#row = next(rows)
#record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)} 
#print(record)
types=[str, int, float] #lista de tipos a los que quiero convertir cada columna
camion = [{ ncolumna: ty(row[index]) for ncolumna, index, ty in zip(select, indices, types)} for row in rows]
#ncolumna son los nombres de columna, quedan como keys
#index los indices de las columnas seleccionadas
#ty el tipo al que quiero convertir los datos
print(camion)
f.close()