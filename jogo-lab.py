# Solicita ao usuário que pense em um número e o insira
y = input("Digite um número inteiro entre 0 e 1024: ")
x = int(y)

# Define os limites inicial e final
a = 0
b = 1024
tentativas = 0  # Contador de tentativas

# Verifica se o número é 0 ou 1024 antes de iniciar a busca
if x == 0:
    print("Seu número é 0. Obrigado por jogar.")
elif x == 1024:
    print("Seu número é 1024. Obrigado por jogar.")
else:
    while True:
        # Calcula o valor médio entre a e b
        n = (a + b) // 2
        tentativas += 1

        # Verifica se encontramos o número
        if n == x:
            print(f"Seu número é {n}. Obrigado por jogar! Adivinhei em {tentativas} tentativas.")
            break
        # Ajusta o limite inferior ou superior conforme a comparação
        elif n < x:
            a = n
        else:
            b = n
