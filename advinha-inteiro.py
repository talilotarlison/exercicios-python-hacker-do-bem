def guess_number():
    # Definindo os valores iniciais
    a = 65
    b = 128
    t = 0
    
    print("Pense em um número inteiro entre 0 e 128.")
    
    while True:
        # Calcula o número médio entre a e b
        M = (a + b) // 2
        t += 1
        
        # Pergunta ao jogador se o número está correto
        response = input(f"O número que você pensou é {M}? (s para sim, n para não): ")
        
        if response.lower() == 's':
            print(f"O número que você pensou é {M} e eu adivinhei em {t} tentativas.")
            break
        elif t == 6:
            print("Desculpe, não consegui adivinhar o número em 6 tentativas.")
            break
        else:
            # Pergunta ao jogador se M é maior que o número correto
            response = input(f"O número {M} é maior que o número correto? (s para sim, n para não): ")
            
            if response.lower() == 's':
                b = M  # Ajusta a extremidade superior
            else:
                a = M  # Ajusta a extremidade inferior
guess_number()