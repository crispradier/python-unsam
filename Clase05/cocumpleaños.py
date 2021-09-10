import random
from collections import Counter
def cumples(n):
    cumples=[random.randint(1,365) for n in range(n)]
    return Counter(cumples).most_common(1)[0][1]>1

def prob_cumples(N):
    repetidos=sum([cumples(30) for x in range(N)])
    prob=repetidos/N
    return prob   

print(prob_cumples(100)) #0,66 a 0,73 con 30 personas
#con 23 personas está cerca de 0,5