# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 10: Faça um programa que mostre as tabuadas dos números de 1 a 10.

import os


os.system('cls')

# Título
print('=' * 50)
print('EXERCÍCIO 10 - TABUADA de 1 a 10')
print('=' * 50)

# Processamento e saída
for numero in range(1, 11):
    print('-' * 50)
    print(f'Tabuada de {numero}:')
    for i in range(1,11):
        resultado = numero * i
        
        print(f'{numero} x {i} = {resultado}')
print('-' * 50)