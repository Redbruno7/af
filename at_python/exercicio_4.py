# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 4: FAÇA UM PROGRAMA QUE LEIA CINCO GRUPOS DE QUATRO VALORES (A, B, C, D) E MOSTRE-OS NA ORDEM LIDA. 
# EM SEGUIDA, MOSTRE-OS EM ORDEM CRESCENTE E DECRESCENTE.

import os


os.system('cls')

# Título
print('='*70)
print('EXERCÍCIO 4')
print('='*70)

# Entrada
grupos = [] # Lista para armazenar grupos

# Processamento
for i in range(1, 6): # Loop para leitura de 5 grupos
    print(f'Grupo {i}: ')
    valores = [] # Lista temporária para os valores de cada grupo
    for j in range(4): # Loop para leitura de valores
        valor = int(input(f'Digite o valor {j + 1} de 4: ')) # Leitura de cada valor
        valores.append(valor) # Adiciona valor à lista do grupo
    grupos.append(valores) # Adiciona lista de valores ao grupo principal

# Saída ordenada
print('-'*70)
print(f'Valores na ordem de inserção:')
for i, valores in enumerate(grupos, start=1): # Imprime grupos em ordem de entrada
    print(f'Grupo {i}: {valores}') # Imprime valores em ordem de entrada

# Saída ordenada crescente
print('-'*70)
print(f'Valores em ordem crescente:')
for i, valores in enumerate(grupos, start=1):
    print(f'Grupo {i}: {sorted(valores)}') # sorted(): exibição crescente

# Saída ordenada decrescente
print('-'*70)
print(f'Valores em ordem decrescente:')
for i, valores in enumerate(grupos, start=1):
    print(f'Grupo {i}: {sorted(valores, reverse=True)}') # sorted(reverse = True): inversão de exibição
print('='*70)