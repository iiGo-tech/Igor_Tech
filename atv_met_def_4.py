# Elabore um programa para calcular a velocidade de três objetos diferentes (com velocidade constante).
# Conhecemos (são dados digitados pelo usuário), para cada objeto, a distância percorrida e o tempo que 
# necessitou para percorrer essa distância. Utilize um método geral que calcule e retorne a velocidade de 
# um objeto, fornecidos como parâmetros os dados de distância e tempo.

def calc_velocidade(distancia, temp):
    vel = distancia / temp
    
    return vel

dist1 = float(input("Digite a distância do primeiro objeto: "))
temp1 = float(input("Digite o tempo do primeiro objeto: "))
dist2 = float(input("Digite a distância do segundo objeto: "))
temp2 = float(input("Digite o tempo do segundo objeto: "))
dist3 = float(input("Digite a distância do terceiro objeto: "))
temp3 = float(input("Digite o tempo do terceiro objeto: "))

vel1 = calc_velocidade(dist1, temp1)
vel2 = calc_velocidade(dist2, temp2)
vel3 = calc_velocidade(dist3, temp3)

print(f"A velocidade do primeiro objeto é: {vel1: .2f}")
print(f"A velocidade do segundo objeto é: {vel2: .2f}")
print(f"A velocidade do terceiro objeto é: {vel3: .2f}")