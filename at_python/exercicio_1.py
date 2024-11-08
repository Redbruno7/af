# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os

os.system('cls')

# Título
print('='*60)
print('EXERCÍCIO 1 - SELEÇÃO DE NÚMEROS EM INTERVALO COM OPERAÇÃO')
print('='*60)

# Entrada
print()
print('=' * 60)
print('Números entre 1000 e 2000 divisíveis por 11 com resto 5:')
print('=' * 60)

# Processamento e Saída
for numero in range(1000, 2000):
    if (numero % 11 == 5):
        print(f'{numero}')
print('='*60)