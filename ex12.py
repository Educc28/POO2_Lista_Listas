import statistics

lst = []
lst2 = []
soma = 0
count = 0

n = int(input("Quantos alunos? "))

for i in range(0, n):
    ele = int(input("Insira a idade: "))
    ele2 = float(input("Insira a altura: "))

    lst2.append(ele)
    lst2.append(ele2)

    if len(lst2) == 2:
        lst.append(lst2)
        lst2 = []

for i in range(0, len(lst)):
    soma = soma + lst[i][1]
mean = soma/len(lst)


for j in range(0, len(lst)):
    if lst[j][0] >= 13:
        if lst[j][1] <= mean:
            count = count + 1

print(lst)
print(count)
