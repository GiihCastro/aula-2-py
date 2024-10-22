frutas = ["Abacaxi", "Melancia", "Uva", "Banana", "Maçã"]

for i in range(5):
    while True:
        fruta = input(f"Digite a fruta {i + 1}: ")
        if fruta in frutas:
            print("Fruta já existe na lista!")
        else:
            frutas.append(fruta)
            print("Fruta adicionada com sucesso")
            break

for fruta_da_vez in frutas:
    print(f"Nome da Fruta: {fruta_da_vez}")