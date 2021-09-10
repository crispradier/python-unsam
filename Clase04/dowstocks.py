import csv
f = open('Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row=next(rows)
types=[str, float, tuple, str, float, float, float, float, int] #como hago el tuple? primero .split('/')
#converted=[ty(val.split('/')) for ty, val in zip(types, row)] # no funciona porque split devuelve listas
record=dict(zip(headers, converted))
print(record)
f.close()
