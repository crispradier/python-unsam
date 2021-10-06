import os
import sys

def archivos_png(directorio):
    pngs=[]
    for files in os.walk(directorio):
        for name in files:
            if type(name)==list:
                for f in name:
                    if f.endswith('.png'):
                        pngs.append(f)
    print(pngs)

        
if __name__=='__main__':
    if len(sys.argv)==2:
        archivos_png(sys.argv[1])
    else:
        archivos_png('../Data/ordenar')
