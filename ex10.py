import statistics

lst = []
lst2 = []
lst3 = []


for i in range(0, 10):
    ele = int(input("Insira o numero inteiro: "))
    lst.append(ele)

for j in range(0, 10):
    ele = int(input("Insira o numero inteiro para a segunda lista: "))
    lst2.append(ele)


for k in range(0, 10):
    lst3.append(lst[k])
    lst3.append(lst2[k])

print(lst3)
