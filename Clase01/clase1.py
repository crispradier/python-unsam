
#saludo.py
d=input('ingrese nombre\n')
print('Hola', d)

lista = [1,2,3]

copia = lista

lista.pop()

print(copia)

#cadenas
s = '  Hello '
t = s.strip()     # 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'
s.endswith(suffix)     # Verifica si termina con el sufijo
s.find(t)              # Primera aparición de t en s (o -1 si no está)
s.index(t)             # Primera aparición de t en s (error si no está)
s.isalpha()            # Verifica si los caracteres son alfabéticos
s.isdigit()            # Verifica si los caracteres son numéricos
s.islower()            # Verifica si los caracteres son minúsculas
s.isupper()            # Verifica si los caracteres son mayúsculas
s.join(slist)          # Une una lista de cadenas usando s como delimitador
s.lower()              # Convertir a minúsculas
s.replace(old,new)     # Reemplaza texto
s.split([delim])       # Parte la cadena en subcadenas
s.startswith(prefix)   # Verifica si comienza con un sufijo
s.strip()              # Elimina espacios en blanco al inicio o al final
s.upper()              # Convierte a mayúsculas