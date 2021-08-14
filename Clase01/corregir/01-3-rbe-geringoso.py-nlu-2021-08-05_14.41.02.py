cadena = input("Introduzca una palabra para pasar a Geringoso:\n") 
#cadena=cadena.lower()
capadepenapa = ''
for c in cadena:
    capadepenapa = capadepenapa + c
    # if c in 'aeiou':
    #     capadepenapa = capadepenapa  + "p" + c
    if c == "a" or c == "A":
        capadepenapa = capadepenapa  + "pa"
    elif c == "e" or c == "E":
        capadepenapa = capadepenapa  + "pe"
    elif c == "i" or c == "I":
        capadepenapa = capadepenapa  + "pi"
    elif c == "o" or c == "O":
        capadepenapa = capadepenapa  + "po"
    elif c == "u" or c == "U":
        capadepenapa = capadepenapa  + "pu"
        
print("En geringoso: ", capadepenapa)
