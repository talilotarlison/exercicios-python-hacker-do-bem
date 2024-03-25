import random

numero_aleatorio = random.randint(1, 10)  # Gera um número entre 1 e 10
contador =0

while numero_aleatorio != 7:
  numero_aleatorio = random.randint(1, 10)  # Gera um número entre 1 e 10
  contador = contador + 1
  print(f"Número aleatório gerado: {numero_aleatorio}")



print(f"Numero correto {numero_aleatorio} em  {contador} tentativas!")