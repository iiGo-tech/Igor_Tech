# Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:

# não-eleitor (abaixo de 16 anos)
# eleitor obrigatório (entre 18 e 65 anos) 
# eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)

idd = int(input("Digite sua idade: "))

if idd < 16:
    print("Não-eleitor")
    
elif (16 <= idd < 18) or (idd > 65):
    print("Eleitor facultativo")
    
else:
    print("Eleitor obrigatório")