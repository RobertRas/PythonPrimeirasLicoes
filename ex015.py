#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("insira uma letra: ")

vogais = ["a", "e", "i", "o", "u"]


if letra in vogais:
    print("{} é uma vogal!".format(letra))
else:
    print("{} é consoante!".format(letra))