produtos = []

for i in range(10):
    while True:
        produto = input(f"Digite o produto {i + 1}: ")
        if produto in produtos:
            print("Esse produto já existe na lista!")
        else:
            produtos.append(produto)
            print("Produto adicionado com sucesso")
            break

for produto_da_vez in produtos:
    if (produto_da_vez.lower()) == "sabonete":
        print("Existe um sabonete na sua lista, parabéns!")