# Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a altura de 
# cada pessoa, calcule e mostre a altura média das mulheres e dos homens separadamente. 
# Utilize o comando de repetição que desejar

manos_soma = minas_soma = manos_qtd = minas_qtd = 0

num = 0
quant = int(input("Nesse rolê tem quantos? "))

while num < quant:
    sex = input("Mano ou mina? 🤨 (M/F): ").upper()
    alt = float(input("Fáfavô, quanto medes: "))
    
    if sex == "M":
        manos_soma += alt
        manos_qtd += 1
        
    elif sex == "F":
        minas_soma += alt
        minas_qtd += 1
        
    num += 1

print(f"Média de manos, lá eles 🤨🏳‍🌈: ", manos_soma / manos_qtd if manos_qtd else 0)
print(f"Média de minas, lá elas 🤨🏳‍🌈: ", minas_soma / minas_qtd if minas_qtd else 0)