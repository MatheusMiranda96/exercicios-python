# Desafio do curso em video
# Crie um programa que leia um número real e mostre sua porção inteira.

from math import trunc

n = float(input("Digite um número: "))
pi = trunc(n) # floor mostra parte inteira do valor.

print (f"Parte inteira do número: {pi}")