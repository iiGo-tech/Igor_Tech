#  Faça um programa em Python que solicite ao usuário, enquanto o mesmo desejar, números e armazene-os em uma lista. 
# Após a entrada de dados, somar os valores da lista, calcular e mostrar a média.
# Calcule e mostre quantos números armazenados na lista estão acima da média.

numeros = []

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    numero = float(entrada)
    numeros.append(numero)
    
soma = sum(numeros)
media = soma / len(numeros) if numeros else 0

print(f"Soma dos numeros: {soma}")
print(f"Média dos números: {media}")

acima_da_media = sum(1 for num in numeros if num > media)

print(f"Números acima da média: {acima_da_media}")
