import datetime
def vida_en_segundos(fecha_nac):
    '''Toma una fecha en formato 'dd/mm/AAAA' y devuelve los segundo vividos'''
    ahora=datetime.datetime.now()
    fecha=datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
    delta=ahora-fecha
    return delta.total_seconds() 

if __name__=='__main__':
    print(vida_en_segundos('28/03/2007'))



