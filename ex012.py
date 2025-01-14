#Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input("insira o primeiro valor:"))
num2 = int(input("insira o segundo valor:"))

if num1 > num2:
    print("{} é maior".format(num1))
else:
    print("{} é maior".format(num2))