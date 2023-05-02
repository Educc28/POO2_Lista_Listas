import statistics

dct = {}
loop = True
n = int(input("Quantos atletas voce quer colocar? "))

for i in range(0, n):
    nome = input("Insira o nome do atleta: ")
    primeiro = int(input("Insira o valor do primeiro salto: "))
    segundo = int(input("Insira o valor do segundo salto: "))
    terceiro= int(input("Insira o valor do terceiro salto: "))
    quarto = int(input("Insira o valor do quarto salto: "))
    quinto = int(input("Insira o valor do quinto salto: "))

    dct[nome] = [primeiro, segundo, terceiro, quarto, quinto]

while loop == True:
    atleta = input("Insira o nome do atleta a ser analisado: ")
    for i, v in dct.items():
        if atleta == i:
            print(f"\nAtleta: {atleta}")
            print(f"Primeiro Salto: {v[0]} m")
            print(f"Segundo Salto: {v[1]} m")
            print(f"Terceiro Salto: {v[2]} m")
            print(f"Quarto Salto: {v[3]} m")
            print(f"Quinto Salto: {v[4]} m" )

            print("\nResultado Final: ")
            print(f"Atleta: {atleta}")
            print(f"Saltos: {v[0]} - {v[1]} - {v[2]} - {v[3]} - {v[4]}")
            print(f"Media dos saltos: {statistics.mean(v)} m")
        elif atleta == "":
            loop = False
            break


    
        