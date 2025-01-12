# crie um programa que leia o saldo de uma pessoa
# e mostre quantos dólares ela pode comprar
# considere o dólar a R$3,27

saldo=float(input("insira o seu saldo: "))
qttDolar= saldo/3.27
formatado= "{:.2f}".format(qttDolar)

print("é possível comprar {} dólares".format(formatado))