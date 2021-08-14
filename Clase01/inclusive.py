frase = 'todos somos programadores'
frase= 'Los hermanos sean unidos porque ésa es la ley primera'
frase='¿cómo transmitir a los otros el infinito Aleph?'
frase='Todos, tu también estas solo' #la coma complica
palabras = frase.split()
inc=[]
for palabra in palabras:
        if palabra.endswith('os'): 
            p=palabra[0:-2]+'es'
            inc.append(p)
        elif palabra.endswith('o'):
            p=palabra[0:-1]+'e'
            inc.append(p)
        else:
            inc.append(palabra)
frase_t = ' '.join(inc)
print(frase_t)
#'todes somes programadores'
#Les hermanes sean unides porque ésa es la ley primera
#¿cómo transmitir a les otres el infinito Aleph?
#Todos, tu también