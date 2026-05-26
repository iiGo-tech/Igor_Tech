# Faça um método que receba como parâmetros o Km inicial, Km final, quantidade de litros gastos e preço do litro. 
# Calcule e mostre: 
# - Distância percorrida;
# - Consumo médio;
# - Valor gasto;

# Faça um programa principal que solicite para o usuário o valor da quilometragem inicial, final, a quantidade 
# de litros gastos e o preço do litro e mostre a distância percorrida, 
# o consumo médio e o valor gasto, para isso utilize o método definido acima.

def viagem(km_i, km_f, litros, preco):
    
    dist = km_f - km_i
    consum = dist / litros
    gasto = litros * preco
    
    print("Distancia:", dist, "km")
    print("Consumo médio:", consum, "km/l")
    print("Valor gasto: R$", gasto)
    
km_i = float(input("Km inicial: "))
km_f = float(input("Km final: "))
litros = float(input("Litros usados: "))
preco = float(input("Preço do litro: "))

viagem(km_i, km_f, litros, preco)