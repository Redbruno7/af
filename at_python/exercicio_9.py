# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 9: Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

import os


os.system('cls')

# Título
print('=' * 50)
print('EXERCÍCIO 9 - TABUADA')
print('=' * 50)

# Entrada Contador
tabuada = 0

# Entrada
numero = int(input('Digite um número para ver sua tabuada: '))

# Processamento e saída
print('-' * 50)
print(f'Tabuada de {numero}:')
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
print('=' * 50)