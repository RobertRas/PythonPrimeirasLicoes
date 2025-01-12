num = int(input("insira um valor:"))

print("tabuada de adição")
for i in range(11):
    
    print("{} + {} = {}".format(num, i, num+i))
    
print("tabuada de subtração")
for i in range(11):
    
    print("{} - {} = {}".format(num, i, num-i))
    
    
print("tabuada de divisão")
for i in range(1, 11):
    mult=num*i
    print("{} / {} = {}".format(mult, num, mult/num))
    
    
print("tabuada de multiplicação")
for i in range(11):
    
    print("{} x {} = {}".format(num, i, num*i))