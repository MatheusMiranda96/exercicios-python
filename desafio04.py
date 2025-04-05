# Desafio do curso em video
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.

n = input("Digite algo: ")

print("Tipo primitivo: ", type(n))
print("Letra? ", n.isalpha())
print("Número? ", n.isnumeric())
print("Alphanumerico? ", n.isalnum())
print("As letras são maiusculas? ", n.isupper())
print("As letras são minusculas? ", n.islower())
