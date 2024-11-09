# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 70)
print('EXERCÍCIO 7 - CONTAGEM DE PESSOAS COM 18 ANOS OU MAIS')
print('=' * 70)
print()

# Contador
maioridade = 0

# Iteração entre 10 pessoas
for i in range(1, 11):
    print('=' * 70)

    # Validação idade
    while True:
        idade = int(input(f'Digite a idade da {i}ª pessoa: '))

        if idade >= 0:
            break
        else:
            print('-' * 70)
            print('Idade inválida! Digite um valor positivo.')
            print('-' * 70)
    print('=' * 70)

# Contagem de pessoas com idade >= 18
    if idade >= 18:
        maioridade += 1

# Saída
print()
print('=' * 70)
print(f'Total de pessoas com idade maior ou igual a 18 anos: {maioridade}')
print('=' * 70)