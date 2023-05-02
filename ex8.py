import statistics

lstIdade = []
lstAltura = []

n = 5

for i in range(0, n):
    eleIdade = int(input("Insira a idade: "))
    eleAltura = float(input("Insira a altura: "))

    lstIdade.append(eleIdade)
    lstAltura.append(eleAltura)

lstAltura.reverse()
lstIdade.reverse()

print(lstIdade)
print(lstAltura)