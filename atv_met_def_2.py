# Escreva um método com retorno que receba como parâmetros os lados de um retângulo, calcula e retorna o valor de sua área. 
#  area = lado*lado
# Faça um programa principal que solicite os valores dos lados de um retângulo ao usuário, e utilizando a função definida acima, 
# calcule e mostre o valor de área.

def calcular_area(lado1, lado2):
    area = lado1 * lado2
    return area

lado1 = float(input("Digite o valor do primeiro lado do retângulo: "))
lado2 = float(input("Digite o valor do segundo lado do retângulo: "))
area = calcular_area(lado1, lado2)

print(f"A área do retângulo é: {area}")

    