produtos = (
    ("Arroz", 25.50, 100),
    ("Feijão", 10.00, 50),
    ("Macarrão", 5.00, 200),
    ("Açúcar", 4.50, 150),
    ("Sal", 2.00, 300),
    ("Óleo", 6.00, 80),
    ("Leite", 3.20, 120),
    ("Café", 15.00, 40),
    ("Biscoito", 7.50, 70),
    ("Sabão", 8.00, 60)
)

soma_total = 0

for produto_da_vez in produtos:
    resultado = produto_da_vez[1] * produto_da_vez[2]
    soma_total += resultado

print(f"A quantidade total de produtos em estoque é {soma_total}.")