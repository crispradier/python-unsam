import csv

def parse_csv(iterable, select = None, types=None, has_headers=True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros, opcionalmente se pueden seleccionar las columnas a 
    parsear, asignarle tipos a los datos y procesar archivos con y sin encabezados
    '''
    rows = csv.reader(iterable)
    if not has_headers and select:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    if has_headers:
        headers = next(rows)
    registros = []
    if select:
        indices=[headers.index(header) for header in select]
        headers=select
    i=0
    for row in rows:
        i+=1
        try:
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
        except ValueError as e:
            if not silence_errors:
                print(f'Fila {i}: No pude convertir {row}')
                print(f'Fila {i}: Motivo: {e}')
    return registros





