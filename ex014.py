#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("informe seu sexo sendo F-feminino e M - masculino  ")

if sexo == "F":
    print("feminino")
elif sexo == "M":
    print("masculino")
else:
    print("sexo inválido")