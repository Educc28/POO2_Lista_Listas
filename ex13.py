import statistics

lst = []
lst2 = []
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']


soma = 0
count = 0

for i in range(0, len(meses)):
    ele = float(input(f"Insira a temperatura de {meses[i]}: "))

    lst2.append(meses[i])
    lst2.append(ele)

    if len(lst2) == 2:
        lst.append(lst2)
        lst2 = []

for j in range(0, len(lst)):
    soma = soma + lst[i][1]
mean = soma/len(lst)


for k in range(0, len(lst)):
    if lst[k][1] >= mean:
        print(lst[k])

