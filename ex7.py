import statistics

lst = []

n = int(input("Quantos numeros voce quer? "))
multiplicar = 1


for i in range(0, n):
    ele = int(input("Insira um numero: "))
    multiplicar = multiplicar * ele
    lst.append(ele)

print(multiplicar)
print("Soma: ", sum(lst))
print("Lista de numeros: ", lst)

