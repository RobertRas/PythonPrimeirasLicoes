"""
- faça um programa que leia a altura e largura de uma parede
- calcule sua área e a quantidade de tinta necessária para pintá-la
- considere que 1L de tinta pinta uma área de 2m°
"""

altura = float(input("insira a altura da parede:"))
largura=float(input("insira a largura da parede:"))
area= altura*largura
qttdLitros= area/2
print("a quantidade de litros necessário para pintar a parede é {}".format(qttdLitros))