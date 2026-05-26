# Faça um programa em Python que solicite ao usuário a placa e o valor da multa de 15 carros. 
# As informações obtidas devem ser armazenadas em 2 listas distintas (observe que cada lista poderá ter apenas 15 
# itens armazenados e que na posição i das duas listas ficarão armazenados: a placa i e o valor de venda i).
# É obrigatório o uso de estrutura de repetição e listas. Calcule e mostre e o valor médio de todas as multas e 
# quantos carros possuem o valor de multa maior ou igual a R$300.00, para isso utilize os dados armazenados nas listas 
# descritas  e estrutura de repetição.

placas = []
multas = []

for i in range(15):
    
    placas.append(input("Digite a placa do carro: "))
    multas.append(float(input("Digite o valor da multa: ")))
    media = sum(multas) / len(multas)
    
    if multas[i] >= 300:
        
        print(f"Carro com placa {placas[i]} tem multa >= R$300.00")
        print(f"Valor médio das multas: R${media:.2f}")
        