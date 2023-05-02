import statistics

lst = []

n = int(input("Quantos numeros voce quer? "))
soma = 0


for i in range(0, n):
    ele = int(input("Insira o numero inteiro: "))
    lst.append(ele)


for j in range(0, len(lst)):
    soma = soma + (lst[j] * lst[j])

print(soma)
