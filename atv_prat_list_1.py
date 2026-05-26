# Faça um programa que contenha 3 listas com os nomes: valores, par e impar. Solicite N números inteiros ao usuário e 
# armazene-os na lista chamada valores 
# (utilize como critério de parada se o usuário deseja continuar). 
# Após a obtenção dos dados, na lista par armazene apenas os números pares da lista valores e na lista ímpar os números ímpares. 
# É obrigatório o uso de estrutura de repetição e listas.
# Exiba os números armazenados nas 3 listas.

val = []
par = []
impar = []



while True:
  val.append(int(input("Digite um número inteiro: ")))

  if input("Deseja continuar? (S/N): ").upper() != "S":
    break
  
for n in val:

  if n % 2 == 0:

    par.append(n)
  else:

    impar.append(n)

print("Valores:", val)
print("Pares:", par)
print("Ímpares:", impar)