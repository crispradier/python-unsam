import random
random.seed(31416)

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 

print(tirada)

caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))