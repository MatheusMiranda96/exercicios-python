# Desafio do curso em video
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


#Utilizando módulo
from math import sqrt

cop = float(input("Comprimento do cateto oposto: "))
cadj = float(input("Comprimento do cateto adjacente: "))

s = (cop ** 2) + (cadj ** 2)
hipo = sqrt(s)

print(f"A medida da hipotenusa é: {hipo}")

'''
# Mesma resolução sem a utilização de módulo

cop = float(input("Comprimento do cateto oposto: "))
cadj = float (input("Comprimento do cateto adjacente: "))

s = (cop ** 2) + (cadj ** 2)
hipo = s ** (1/2)

print(f"A medida da hipotenusa é: {hipo}")
'''