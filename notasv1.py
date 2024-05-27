import random

# Lista de nomes fictícios para os alunos
nomes_alunos = ["Pedro", "Ana", "Lucas", "Carla", "Rafael", "Juliana", "Marcos", "Isabela", "Gustavo", "Larissa"]
notas = []

# Crie notas aleatórias para 10 alunos
for i in range(10):
    nome_aluno = random.choice(nomes_alunos)
    idade_aluno = random.randint(10, 18)  # Idade entre 10 e 18 anos
    media_aluno = round(random.uniform(5, 10), 2)  # Média entre 5 e 10 (com 2 casas decimais)
    
    notas.append({"nome": nome_aluno, "idade": idade_aluno, "media": media_aluno})

# Exemplo de acesso aos dados de um aluno específico:
primeiro_aluno = notas[2]  # Índice 2 representa o terceiro aluno (índices começam em 0)
print(f"Nome: {primeiro_aluno['nome']}, Idade: {primeiro_aluno['idade']}, Média: {primeiro_aluno['media']}")
