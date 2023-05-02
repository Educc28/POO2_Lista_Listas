import statistics

lst = []


salario = 1
totalGasto = 0
valorMinimo = 0
colaboradores = 0
maiorAbono = 0

print("Projeção de gastos com o abono")
while salario != 0:
    salario = float(input("Salário: "))
    if salario == 0:
        break
    else:
        abono = salario * 0.2
        if abono < 100:
            abono = 100
            valorMinimo = valorMinimo + 1
        info = [salario, abono]
        lst.append(info)
        totalGasto = totalGasto + abono
        colaboradores = colaboradores + 1
        if abono > maiorAbono:
            maiorAbono = abono
print("Salário    -    Abono")
for i in lst:
    print(f"R${i[0]}    -    R${i[1]}")
print(f"Foram processados {colaboradores} colaboradores")
print(f"Total gasto com abonos: R${totalGasto}")
print(f"Valor mínimo pago a {valorMinimo} colaboradores")
print(f"Maior valor de abono pago: R${maiorAbono}")