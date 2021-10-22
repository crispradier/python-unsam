from vigilante import vigilar
import informe_final
import formato_tabla
import csv

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    rows=(dict(zip(headers, row)) for row in rows)
    for row in rows:
        yield row

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(rows, nombres):
    rows=(row for row in rows if row['nombre'] in nombres)
    for row in rows:
        yield row

def ticker(camion_file, log_file, fmt):
    formateador = formato_tabla.crear_formateador(fmt)
    camion = informe_final.leer_camion(camion_file)
    lines = vigilar(log_file)
    rows = parsear_datos(lines)
    rows = filtrar_datos(rows, camion)
    formateador.encabezado(['Nombre', 'Precio','Volumen'])
    for row in rows:
        valores=[str(y) for x,y in row.items()]
        formateador.fila(valores)


if __name__ == '__main__':
    ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')
#     import informe_final
#     camion = informe_final.leer_camion('../Data/camion.csv')
#     lines = vigilar('../Data/mercadolog.csv')
#     rows = parsear_datos(lines)
#     rows = filtrar_datos(rows, camion)
#     for row in rows:
#         print(row)