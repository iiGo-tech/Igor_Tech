# Faça um programa que:
# Leia duas listas com 5 inteiros cada.
# Checa quais elementos da segunda lista são iguais a algum elemento da primeira lista.
# Se não houver elementos em comum, o programa deve informar isso.

list1 = []
list2 = []

print("Digite 5 números inteiros: ")
for i in range(5):
    list1.append(int(input(f"Número {i+1}: ")))
    print("Digite mais 5 números inteiros: ")
    
for i in range(5):
    list2.append(int(input(f"Número {i+1}: ")))
    print("Checando elementos em comum...")
    
    for num in list2:
        if num in list1:
            print(f"O número {num} está em ambas as listas.")
        
        if not any(num in list1 for num in list2):
            print("Não há elementos em comum entre as listas.")
            