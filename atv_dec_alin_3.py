# 

nome = input("Digite o nome do produto: ")
val = float(input("Digite o valor de compra: R$ "))

if val < 10:
    venda = val * 1.70
elif val < 30:
    venda = val * 1.50
elif val < 50:
    venda = val * 1.40
else:
    venda = val * 1.30

print("Produto:", nome)
print("Valor de venda: R$ {:.2f}".format(venda))