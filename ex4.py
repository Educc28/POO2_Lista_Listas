import statistics

lst = []
vowels = ['a', 'e', 'i', 'o', 'u']
consonantNumber = 0

n = int(input("Quantos letras voce quer? "))

for i in range(0, n):
    ele = input("Insira uma letra: ")
    lst.append(ele)

for j in lst:
    for k in vowels:
        if j == k:
            consonantNumber = consonantNumber + 1


print(consonantNumber)