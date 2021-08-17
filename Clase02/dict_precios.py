precios = {}  # Empezamos con un diccionario vacío

with open('../Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        try:
            precios[row[0]] = float(row[1])
        except IndexError:
            pass

print(precios)