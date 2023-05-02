import statistics

lst = []

n = int(input("Quantos numeros voce quer? "))

for i in range(0, n):
    ele = int(input("Insira o numero inteiro: "))
    lst.append(ele)


print(lst)
lstMean = statistics.mean(lst)
print(lstMean)