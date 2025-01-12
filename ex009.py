"""
faça um algoritmo que leia o salário de um funcionário
e mostre seu valor com 15% de aumento
"""

salario=float(input("insira seu salário:"))
aumento=((15/100)*salario)+salario
print("seu salário com aumento é R${}".format(aumento))