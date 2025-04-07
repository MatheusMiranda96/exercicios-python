# Desafio do curso em video
# Faça um algoritmo que leia o preço de um produto e imprima seu novo preço com 5% de desconto.

prod = float(input("Preço do produto R$: "))
desc = prod - (prod*0.05)

print(f"Preço do produto com desconto: R${desc:.2f}")