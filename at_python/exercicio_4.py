# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 90)
print('EXERCÍCIO 4 - LEITURA DE ELEMENTOS DE GRUPOS '
      'EM ORDEM INSERIDA, CRESCENTE E DECRESCENTE')
print('=' * 90)

# Lista
grupos = []

# Iteração entre 5 grupos
for i in range(1, 6):
    print()
    print('=' * 90)
    print(f'Grupo {i}: ')
    print('=' * 90)

    # Lista temporária para valores de cada grupo
    valores = []

    # Iteração entre 4 valores
    for j in range(1, 5):
        valor = int(input(f'Digite o valor {j} de 4: '))
        valores.append(valor)
    grupos.append(valores)
    print('=' * 90)

# Saída
print()
print('=' * 90)
print(f'Valores na ordem de inserção:')
print('-' * 90)

# Iteração entre os valores dos grupos em ordem inserida
for i, valores in enumerate(grupos, start=1): 
    print(f'Grupo {i}: {valores}')

print('-' * 90)
print(f'Valores em ordem crescente:')
print('-' * 90)

# Iteração entre os valores dos grupos em ordem crescente
for i, valores in enumerate(grupos, start=1):
    print(f'Grupo {i}: {sorted(valores)}')

print('-' * 90)
print(f'Valores em ordem decrescente:')
print('-' * 90)

# Iteração entre os valores dos grupos em ordem decrescente
for i, valores in enumerate(grupos, start=1):
    print(f'Grupo {i}: {sorted(valores, reverse=True)}')
print('=' * 90)