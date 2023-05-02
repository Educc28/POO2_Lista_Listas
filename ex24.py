import statistics
from random import randint


lst = []
dados = [[1,0], [2,0], [3,0], [4,0], [5,0], [6,0]]

for i in range(0, 100):
    valor = randint(1, 6)
    for j in range(0, len(dados)):
        if valor == dados[j][0]:
            dados[j][1] = dados[j][1] + 1
print(dados)
    
    

