def buscar_precio(fruta):
    f = open('../../Data/precios.csv', 'rt')
    x=False
   
    for line in f:
        if fruta in line:
            r=line.split(',')
            print(f'El precio de un cajon de {fruta} es: {r[1]}')
            x=True   
   
    if x==False:
        print(f'{fruta} no figura en el listado de precios.')      
    
    f.close()

buscar_precio('Frambuesa')
buscar_precio('Kale')
