import csv

def parse_csv(nombre_archivo, select = None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros, opcionalmente se pueden seleccionar las columnas a 
    parsear, asignarle tipos a los datos y procesar archivos con y sin encabezados
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        if has_headers:
            headers = next(rows)
        registros = []
        if select:
            indices=[headers.index(header) for header in select]
            headers=select
        for row in rows:
            if not row:    
                continue
            if select:
                row=[row[indice] for indice in indices]
            if types:
                row=[tipo(valor) for tipo, valor in zip(types, row)]
            if has_headers:
                registro = dict(zip(headers, row))
            else:
                registro=tuple(row)
            registros.append(registro)
    return registros

#print(parse_csv('Data/camion.csv', select=['cajones', 'nombre'], types=[int, str]))
#print(parse_csv('Data/precios.csv', types=[str, float], has_headers=False))