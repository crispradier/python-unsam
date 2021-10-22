def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if len(lista)%2==0:
            res=bbinaria_rec(lista[:medio-1],e) or bbinaria_rec(lista[medio:],e)
        else:
            if lista[medio] == e:
                res = True
            else:
                res=bbinaria_rec(lista[:medio-1],e) or bbinaria_rec(lista[medio+1:],e)
    return res

if __name__=="__main__":
    print(bbinaria_rec([0,1,2,3], 3),
        bbinaria_rec([0,1,2,3,4], 2),
        bbinaria_rec([1,2,3],0))