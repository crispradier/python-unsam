def sumar_enteros_ciclo(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma=0
    if desde<hasta:
        intervalo=[x for x in range(desde, hasta+1)]
        for num in intervalo:
            suma+=num
    return suma


def sumar_enteros_cte(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma=0
    if desde<hasta:
        tri=(hasta*(hasta+1))/2
        vacio=((desde-1)*(desde))/2
        suma=tri-vacio
    return suma

