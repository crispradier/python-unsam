def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0,e) #agrego el elemento e al principio de la lista invertida
    return invertida

def propagar(lista):
    prop=[]  #lista vacía para guardar propagacion si modificar la original
    propagacion=False  # en esta variable se guarda el estado, en propagacion o no
    for x in lista:
        if x==1:
            prop.append(x)
            propagacion=True
        elif x==0 and propagacion==True:
            prop.append(1)
        elif x==0 and propagacion==False:
            prop.append(x)
        else:
            prop.append(x)
            propagacion=False
    if 0 in prop:                        # si sigue habiendo ceros vuelve a recorrerse la lista, si no no vale la pena
        listalista=invertir_lista(prop) #inverti para volver a recorrer
        propprop=[]   #nueva lista vacia
        propagacion=False #estado vuelve a false
        for x in listalista:
            if x==1:
                propprop.append(x)
                propagacion=True
            elif x==0 and propagacion==True:
                propprop.append(1)
            elif x==0 and propagacion==False:
                propprop.append(x)
            else:
                propprop.append(x)
                propagacion=False
        prop=invertir_lista(propprop) # reasigno prop, vuelvo a invertir para volver al orden original
    return prop

print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
print(propagar([ 0, 0, 0, 1, 0, 0]))