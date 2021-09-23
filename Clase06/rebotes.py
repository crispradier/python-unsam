def rebote(altura):
    r=1
    while r<=10:
        altura=round(0.6*altura, 4)
        print('{} {}'. format(r, altura))
        r+=1

rebote(100)

# out:
# 1 60.0
# 2 36.0 
# 3 21.6 
# 4 12.96
# 5 7.776
# 6 4.6656
# 7 2.7994
# 8 1.6796
# 9 1.0078
# 10 0.6047