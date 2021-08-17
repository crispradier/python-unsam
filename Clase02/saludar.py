# def saludar(nombre):
#     'Saludar a alguien'
#     print(f'Hola {nombre}')

# saludar('Paula')
# help(saludar)

'''
solucion de sofi a dict geringoso

def geringoso(cadena):
    capadepenapa = ''
    vocales=['a','e','i','o','u']
    for c in cadena:
            if c in vocales:
                capadepenapa=capadepenapa+c+'p'+c
            else:
                capadepenapa=capadepenapa+c   
    return capadepenapa

def diccionario_geringoso(palabras):
       
    lista_diccionario = []
    lista_palabras = palabras
    lista_geringoso = []
   
    for c in lista_palabras:
        lista_geringoso.append(geringoso(c))
    
    for i in range(0,len(lista_palabras)):
        lista_diccionario.append((lista_palabras[i],lista_geringoso[i]))

    d = dict(lista_diccionario)
    print(d)
    
diccionario_geringoso(['banana', 'manzana', 'mandarina'])
'''
