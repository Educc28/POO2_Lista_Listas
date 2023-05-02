import statistics

def porcentagem(votos, totalVotos):
    media = votos/totalVotos
    media = media*100
    return media

def main():
    dct = {1 : ["Windows Server", 0],
           2: ["Unix", 0],
           3: ["Linux", 0],
           4: ["Netware", 0],
           5: ["Mac OS", 0],
           6: ["Outro", 0]
           
           }
    voto = 1
    quantVotos = 0
    maiorMedia = 0
    melhorJogador = 0
    maiorVoto = 0

    print("Qual o melhor Sistema Operacional para uso em servidores?")
    print("As possíveis respostas são:")
    print("""
    1- Windows Server
    2- Unix
    3- Linux
    4- Netware
    5- Mac OS
    6- Outro    
    """)
    while voto != 0:
        voto = int(input("Vote (0=fim): "))

        if voto > 0 and voto <= 6:
            quantVotos = quantVotos + 1
            if voto in dct:
                dct[voto][1] = dct[voto][1] + 1
        elif voto < 0 or voto > 6:
            print("Informe um valor entre 1 e 6 ou 0 para sair!")
        else:
           
            print("Sistema Operacional          Votos           %")
            for k, v in dct.items():
                media = porcentagem(v[1], quantVotos)
                if media > maiorMedia:
                    maiorMedia = media
                    melhorJogador = v[0]
                    maiorVoto = v[1]
                print(f"{k}                 {v[1]}           {media}%")
            print(f"Total:                  {quantVotos}")
            print(f"O Sistema Operacional mais votado foi o {melhorJogador}, com {maiorVoto} votos, correspondendo a {maiorMedia}% dos votos.")


if __name__ == "__main__": #Início do código
    main()
