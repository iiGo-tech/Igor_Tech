# Elabore um programa em Python que leia os salários de 10 trabalhadores de uma empresa e os armazene em uma lista. 
# Após a entrada de dados, o programa deverá:

# Calcular a média desses salários.
# Determinar o maior dos salários desta empresa.
# Contar os salários menores que R$850,00.
# Exibir todos os resultados na tela.

salarios = []

for i in range(10):
    
    salario = float(input(f"Digite o salário do trabalhador {i + 1}: "))
    salarios.append(salario)

media_salarios = sum(salarios) / len(salarios)
maior_salario = max(salarios)
menores_850 = sum(1 for salario in salarios if salario < 850)

print(f"Média dos salários: R$ {media_salarios:.2f}")
print(f"Maior salario: R$ {maior_salario:.2f}")
print(f"Quantidade de salários menores que R$ 850,00: {menores_850}")
