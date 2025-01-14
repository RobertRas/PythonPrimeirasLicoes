#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num=int(input("insira um valor:"))

if num > 0:
    print("{} é positivo".format(num))
elif num < 0:
    print("{} é negativo".format(num))
else:
    print("{} é igual a zero".format(num))