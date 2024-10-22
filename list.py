# Estrutura obrigatória da lista, separada por , e em [] 
frutas = ["Abacaxi", "Melancia", "Uva", "Banana", "Maçã"] # Str
idades = [29, 42, 35, 28, 14, 17, 18, 20] # Int
notas = [4.2, 5.8, 9.7, 6, 7.4, 6.5] # Float
habilitados = [True, True, False, True, False] # Bool
pessoa = ["João", 32, 1.81, True] # Misturado, NÃO FAÇA
pessoa2 = {
    "nome": "João",  
    "idade": 32, 
    "altura": 1.81, 
    "habilitado": True} # Usando dicionário

frutas = ["Abacaxi", "Melancia", "Uva", "Banana", "Maçã"]
frutas[4] = "Laranja" # Muda o item
print(frutas[2]) 
print(frutas)
print(len(frutas))

print(frutas[len(frutas) - 1]) # Último item da lista
print(frutas[-1]) # Jeito mais fácil

# Métodos de Lista

frutas2 = ["Abacaxi", "Melancia", "Uva", "Banana", "Maçã"]
nome = "giih"
print(nome.upper()) # Deixa maísculo

frutas2.append("Laranja") # Adiciona um item ao final da lista
frutas2.insert(2, "Acerola") # Adiciona um item na posição desejada

frutas.pop() # Remove o último item
frutas.pop(2) # Remove o item desejado pela posição
frutas.remove("Banana") # Remove o item por nome


