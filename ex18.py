import statistics

def porcentagem(votos, totalVotos):
    media = votos/totalVotos
    media = media*100
    return media

def main():
    dct = {}
    voto = 1
    quantVotos = 0
    maiorMedia = 0
    melhorJogador = 0
    maiorVoto = 0

    print("Enquete: Quem foi o melhor jogador?")
    while voto != 0:
        voto = int(input("Número do jogador (0=fim): "))

        if voto > 0 and voto <= 23:
            quantVotos = quantVotos + 1
            if voto in dct:
                dct[voto] = dct[voto] + 1
            else:
                dct[voto] = 1
        elif voto < 0 or voto > 23:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
        else:
            print("Resultado da Votação: ")
            print(f"Foram computados {quantVotos} votos")
            print("Jogador          Votos           %")
            for k, v in dct.items():
                media = porcentagem(v, quantVotos)
                if media > maiorMedia:
                    maiorMedia = media
                    melhorJogador = k
                    maiorVoto = v
                print(f"{k}                    {v}           {media}%")
            print(f"O melhor jogador foi o número {melhorJogador}, com {maiorVoto} votos, correspondendo a {maiorMedia}% do total de votos.")


if __name__ == "__main__": #Início do código
    main()
