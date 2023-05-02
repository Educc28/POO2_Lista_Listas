import statistics

lstCarro = []
lstConsumo = []
menorConsumoLitro = 0
consumo1000 = 0
menorConsumoCarro = ""
preco = 0


for i in range(0, 5):
    print(f"Veículo {i+1}")
    nome = input("Nome: ")
    consumo = float(input("Km por Litro: "))
    lstCarro.append(nome)
    lstConsumo.append(consumo)

print("Relatorio Final: ")

for i in range(0, len(lstCarro)):
    consumo1000 = 1000/lstConsumo[i]
    preco = 2.25 * consumo1000

    if consumo1000 < menorConsumoLitro or menorConsumoLitro == 0:
        menorConsumoLitro = consumo1000
        menorConsumoCarro = lstCarro[i]

    print(f"{i} - {lstCarro[i]} - {lstConsumo[i]} - {consumo1000} litros - R${preco}")
print(f"O menor consumo é do {menorConsumoCarro}.")


