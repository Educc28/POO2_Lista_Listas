import statistics

lst = []
lst2 = []
lst3 = []
lst4 = []

for i in range(0, 10):
    ele = int(input("Insira o numero inteiro: "))
    lst.append(ele)

for j in range(0, 10):
    ele = int(input("Insira o numero inteiro para a segunda lista: "))
    lst2.append(ele)

for j in range(0, 10):
    ele = int(input("Insira o numero inteiro para a terceira lista: "))
    lst3.append(ele)

for l in range(0, 10):
    lst4.append(lst[l])
    lst4.append(lst2[l])
    lst4.append(lst3[l])

print(lst4)
