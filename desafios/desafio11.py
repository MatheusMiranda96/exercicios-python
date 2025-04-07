# Desafio do curso em video
# Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados.

alt = float(input("Altura: "))
lgr = float(input("Largura: "))
ar = alt * lgr
tinta = ar / 2

print(f"Área total: {ar} metros quadrados.")
print(f"Quantidade de tinta: {tinta} litros")
