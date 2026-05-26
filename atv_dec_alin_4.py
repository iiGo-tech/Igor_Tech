# Elabore um programa em Python que implemente uma calculadora com as funções de somar, subtrair, 
# multiplicar e dividir. O programa deverá solicitar ao usuário os dois valores, e perguntar qual a 
# operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) e a seguir calcular e mostrar o resultado.

# Lê os valores
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

# Lê a operação
op = input("Digite a operação (soma +, sub -, mult *, div /): ")

# Verifica e calcula
if op == "+":
    resultado = a + b
elif op == "-":
    resultado = a - b
elif op == "*":
    resultado = a * b
elif op == "/":
    if b != 0:
        resultado = a / b
    else:
        print("Erro: divisão por zero")
        resultado = None
else:
    print("Operação inválida")
    resultado = None

# Mostra o resultado
if resultado is not None:
    print("Resultado:", resultado)