import random

numero_aleatorio = random.randint(1, 10)  # Gera um número entre 1 e 10
print(f"Número aleatório gerado: {numero_aleatorio}")


numero_aleatorio1 = random.randrange(0, 10, 2)  # Gera números pares entre 0 e 8
print(f"Número aleatório gerado: {numero_aleatorio1}")

numero_aleatorio2 = random.uniform(10, 20)  # Gera um número entre 10 e 20
print(f"Número aleatório gerado: {numero_aleatorio2}")