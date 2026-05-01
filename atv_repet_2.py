# Faça um programa em Python que imprima os números de 1 a 50 
# de 1 em 1 e de 
# 52 a 100 de 2 em 2.

# Numeros de 1-50 de 1 em 1
for num in range(1, 51):
    print(num)

# Numeros de 52-100 de 2 em 2

for num in range(52, 101):
    if num %2 == 0:
        print(num)