
def geringoso(cadena):
    capadepenapa = ''
    vocales=['a','e','i','o','u']
    for c in cadena:
            if c in vocales:
                capadepenapa=capadepenapa+c+'p'+c
            else:
                capadepenapa=capadepenapa+c   
    return capadepenapa

def dict_geringoso(lista):
    diccionario={}
    for palabra in lista:
        diccionario[palabra]=geringoso(palabra)
    return diccionario

print(dict_geringoso(['banana', 'manzana', 'mandarina']))
# {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}