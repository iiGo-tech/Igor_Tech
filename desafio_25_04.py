import random

numero_estranho = random.randint(0, 100)

while True:
    tenta = int(input("Tente adivinhar o número (0 a 100): "))

    if tenta < numero_estranho:
        print("O número é MAIOR que isso rapai.")
    elif tenta > numero_estranho:
        print("O número é MENOR que isso rapai.")
    else:
        print("Parabéns! Você acertou! Tu é fera papai!")
        break