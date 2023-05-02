import statistics

lst = []
resposta = ['sim', 'não']
count = 0

while True:
    ele = input("Telefonou para a vitima? ")
    if ele == 'sim':
        count = count + 1
        break
    elif ele == 'não':
        break
    else:
        print("Responda com sim ou não, tente novamente.")

while True:
    ele = input("Esteve no local do crime? ")
    if ele == 'sim':
        count = count + 1
        break
    elif ele == 'não':
        break
    else:
        print("Responda com sim ou não, tente novamente.")

while True:
    ele = input("Mora perto da vitima? ")
    if ele == 'sim':
        count = count + 1
        break
    elif ele == 'não':
        break
    else:
        print("Responda com sim ou não, tente novamente.")

while True:
    ele = input("Devia para a vitima? ")
    if ele == 'sim':
        count = count + 1
        break
    elif ele == 'não':
        break
    else:
        print("Responda com sim ou não, tente novamente.")

while True:
    ele = input("Ja trabalhou para a vitima? ")
    if ele == 'sim':
        count = count + 1
        break
    elif ele == 'não':
        break
    else:
        print("Responda com sim ou não, tente novamente.")


if count == 2:
    print("Suspeita")
elif count == 3 or count == 4:
    print("Cumplice")
elif count == 5:
    print("Assassino")
else:
    print("Inocente")