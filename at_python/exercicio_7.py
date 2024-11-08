# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('='*70)
print('EXERCÍCIO 7 - CONTAGEM DE PESSOAS COM 18 ANOS OU MAIS')
print('='*70)

# Entrada contador
maioridade = 0

# Processamento
for i in range(1, 11):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    print('-'*70)

    if idade >= 18:
        maioridade += 1

# Saída
print(f'Total de pessoas com idade maior ou igual a 18 anos: {maioridade}')
print('='*70)