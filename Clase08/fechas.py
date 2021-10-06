import datetime
def primavera():
    ahora=datetime.date.today()
    primavera=datetime.date(ahora.year,9,21)
    delta=primavera-ahora
    print(delta)
    return delta.days

def dias_habiles(inicio, fin, feriados):
    i=datetime.datetime.strptime(inicio, '%d/%m/%Y')
    f=datetime.datetime.strptime(fin, '%d/%m/%Y')
    menos=[datetime.datetime.strptime(dia, '%d/%m/%Y') for dia in feriados]
    while i!=f+datetime.date(0,0,1):
        if i.weekday()!=5 and i.weekday()!=6:
            if i not in menos:
                print(i)
        i=i+datetime.date(0,0,1)
print(dias_habiles('20/09/2020', '10/10/2020', []))