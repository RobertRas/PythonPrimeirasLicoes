# receber um valor em metros e transformar para centímetros e milímetros
metro = float(input("digite um valor em metros: "))
centimetros = metro*100
mili = metro*1000
print("{} metros equivale a {} centímetros e {} milímetros".format(metro, centimetros, mili))