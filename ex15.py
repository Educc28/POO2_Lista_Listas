import statistics

lst = []
ele = 0

while ele != -1:
    ele = int(input("Insira o numero inteiro: "))
    if ele == -1:
        break
    else:
        lst.append(ele)

media = statistics.mean(lst)
count = 0

print(f'Tamanho: {len(lst)}')
print(f'Lista: {lst}')
print(f'Ordem Inversa: {lst.reverse()}')
print(f'Soma: {sum(lst)}')
print(f'Media: {media}')

for i in range (0, len(lst)):
    if lst[i] > media:
        count = count + 1

print(f'Quantidades acima da media: {count}')

for i in range (0, len(lst)):
    if lst[i] < 7:
        print(f'Valores menores que 7: {lst[i]}')
print("Fim do programa")