# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 9: FAÇA UM ALGORITMO PARA TRANSFORMAR O VALOR CORRESPONDENTE A UM INTERVALO TEMPORAL, 
# EXPRESSO EM HORAS, MINUTOS E SEGUNDOS, NO VALOR CORRESPONDENTE EM SEGUNDOS.

import os


os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 9')
print('='*50)

# Entrada
horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))

# Processamento
total_segundos = (horas * 3600) + (minutos * 60) + segundos

# Saída
print('.'*50)
print(f'O valor corresponde à {total_segundos} segundos.')
print('='*50)