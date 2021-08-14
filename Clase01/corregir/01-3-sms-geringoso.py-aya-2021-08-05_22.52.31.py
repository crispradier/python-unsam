cadena = input("Ingrese una palabra: ")
equivalente_geringoso = {'a':'pa', 'e':'pe','i':'pi','o':'po','u':'pu'} #dict repetitivo aunque funcione
capadepenapa = ""
for letra in cadena: 
    if letra in equivalente_geringoso:
        capadepenapa += letra + equivalente_geringoso[letra]
    else:
        capadepenapa += letra

print(capadepenapa)

