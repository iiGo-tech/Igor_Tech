# Construir um método que receba como parâmetros o valor de uma compra e a quantidade de parcelas e calcula e retorna o valor da parcela, 
# sabendo que a loja acrescenta 5% de juros para as compras parceladas.
# No algoritmo principal, solicite para o usuário o valor de uma compra e a quantidade de 
# parcelas e utilizando o método descrito acima, mostre o valor da parcela.

def calcular_parcela(valor_compra, parcelas):
    
    if parcelas > 1:
        valor_compra = valor_compra * 1.05
    val_parcela = valor_compra / parcelas
    return val_parcela

valor = float(input("Digite o valor da compra: "))
qtd_parcelas = int(input("Digite a quantidade de parcelas: "))
resultado = calcular_parcela(valor, qtd_parcelas)
print(f"Valor de cada parcela: R$ {resultado: .2f}")