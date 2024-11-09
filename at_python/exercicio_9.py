# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 50)
print('EXERCÍCIO 9 - TABUADA')
print('=' * 50)
print()

# Entrada
print('=' * 50)
numero = int(input('Digite um número para ver sua tabuada: '))
print('=' * 50)

# Iteração do número na tabuada e Saída
print()
print('=' * 50)
print(f'Tabuada de {numero}:')
print('-' * 50)
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
print('=' * 50)