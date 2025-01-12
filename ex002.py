#criar um código que leia um número e mostre seu dobro, triplo e raíz quadrada
n = float(input("insira um valor: "))
dobro = n * 2
triplo = n * 3
raiz = n**0.5

print(" o seu dobro é {}, o seu triplo é {} e a sua raíz quadrada é {:.2f}".format(dobro, triplo, raiz))