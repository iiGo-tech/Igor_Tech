#-------------------------------------------------------------------------------------------------------#
# Escreva um programa em Python que solicite ao usuário os valores de três contas de consumo            #
# (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário é suficiente para pagar #
# as três contas, caso não seja apresente a mensagem “Salário insuficiente!”.                           #
# Caso seja, apresente o valor que restou do salário após pagar as contas.                              #
#-------------------------------------------------------------------------------------------------------#

agua = float(input("Coloque sua conta de Aguá: R$ "))
gas = float(input("Coloque sua conta de Gás: R$ "))
inter = float(input("Coloque sua conta de Internet: R$ "))
sal = float(input("Digite seu Salário: R$ "))

if sal < agua + gas + inter:
    print("Salário não suficiente!🤬")
    
else:
    print(f"Restante: R$ {sal - (agua + gas + inter):.2f} olha aí você tem granha, aí sim 😎")