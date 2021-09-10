a = [1,2,3]
print(id(a))
b = a
a = a.append(4)
print(id(b))
print(id(a))