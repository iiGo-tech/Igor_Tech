# Faça um programa em Python que leia um valor n, inteiro e positivo,
# calcule e mostre a seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n

n = int(input("Digite um número POSITIVO (igual o pc lá) inteiro de preferência: "))

soma = 0

for num in range(1, n + 1):
    soma += 1 / num
    
print("Resultado da soma:", soma)