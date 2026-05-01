#Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são positivos 
# e quantos são negativos. Determine, também, qual é o menor desses valores. 
# Utilize o comando de repetição que desejar.

posit = 0
negat = 0
menor = None

quant = int(input("Números que serão colocados: "))
num = 0

while num < quant:
    val = float(input("Coloque um valor: "))
    
    if val >= 0:
        posit += 1
    else:
        negat += 1
        
    if menor is None or val < menor:
        menor = val
        
    num += 1

print("Positivos: ", posit)
print("Negativos: ", negat)
print("Menor: ", menor)
