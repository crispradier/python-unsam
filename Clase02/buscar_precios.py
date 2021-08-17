def buscar_precio(fruta):
    f = open('../Data/precios.csv', 'rt') #cuidado, para que funcione hay que ejecutarlo desde Clase02
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
# El precio de un cajon de Frambuesa es: 34.35
buscar_precio('Kale')
# Kale no figura en el listado de precios.