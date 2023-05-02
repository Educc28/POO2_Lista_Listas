import statistics

lst = []
count = 0
intervals = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699], [700, 799], [800, 899], [900, 999], [1000]]
toCount = []

n = int(input("Quantos salarios voce quer colocar? "))

for i in range(0, n):
    ele = float(input("Insira as vendas semanais: "))
    ele = ele*1.09 + 200
    lst.append(ele)



m = int(input("Indique o valor inicial do interval: "))

for i in range (0, len(intervals)):
    if m == intervals[i][0]:
        value = intervals[i]

for i in range (0, len(lst)):
    if lst[i] >= value[0] and lst[i] <= value[1]:
        count = count + 1

print(f"Quantidade de vendedores que receberam entre o intervalo {value}: {count} ")

