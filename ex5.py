import statistics

lstEven = []
lstOdd = []

n = int(input("Quantos numeros voce quer? "))

for i in range(0, n):
    ele = int(input("Insira um numero: "))

    if ele % 2 == 0:
        lstEven.append(ele)
    else:
        lstOdd.append(ele)

print(lstEven)
print(lstOdd)