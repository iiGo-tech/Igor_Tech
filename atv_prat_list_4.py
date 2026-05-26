# Faça um programa em Python que solicite ao usuário o dia da semana e o volume de chuva correspondente a 10 dias. 
# As informações obtidas devem ser armazenadas em 2 listas distintas (observe que cada lista poderá ter apenas 10 itens 
# armazenados e que na posição i das duas listas ficarão armazenados: o dia da semana i e o volume de chuva i).
# É obrigatório o uso de estrutura de repetição e listas.Em seguida, calcule e mostre o volume médio de chuva apenas do dia de 
# semana igual a quarta-feira e a soma total do volume de chuva, para isso utilize os dados armazenados nas listas. 
# É obrigatório o uso de estrutura de repetição e das listas do exercício descritas anteriormente.

dias = []
volumes = []

for i in range(10):
    
    dias.append(input("Digite o dia da semana: "))
    volumes.append(float(input("Digite o volume de chuva: ")))

quartas = [volumes[j] for j in range(len(dias)) if dias[j].lower() == "quarta-feira"]
media_quart = sum(quartas) / len(quartas) if quartas else 0.0

soma_ttl = sum(volumes)
print(f"Volume médio de chuva na quarta-feira: {media_quart:.2f}")
print(f"Soma total do volume de chuva: {soma_ttl:.2f}")