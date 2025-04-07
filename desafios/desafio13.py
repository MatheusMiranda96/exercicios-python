# Desafio do curso em video
# Faça um algoritmo que leia o salário de uma pessoa e mostre seu novo salário, com 15% de aumento.

sal = float(input("Valor atual do salário R$: "))
aum = sal + (sal*0.15)

print(f"Salário com aumento R$: {aum:.2f}")
