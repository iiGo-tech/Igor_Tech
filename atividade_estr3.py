#-------------------------------------------------------------------------------------------#
# Faça um programa em Python que obtenha o valor de uma compra,                             #
# calcular e mostrar o valor da compra considerando o desconto, conforme descrito abaixo:   #
#                                                                                           #
#                                                                                           #
# Para compras acima de R$ 200 a loja dá um desconto de 20%                                 #
# Para as abaixo disso não tem desconto, mostre o valor da compra.                          #
#-------------------------------------------------------------------------------------------#

val = float(input("Digite o valor da compra: R$ "))

if val > 200:
    desc = val * 0.20
    val_final = val - desc
    
    print(f"Valor original: R$ {val:.2f}")
    print(f"Desconto: R$ {desc:.2f}")
    print(f"Valor Final: R$ {val_final:.2f}")
else:
    print(f"Valor final sem desconto: R$ {val:.2f}")