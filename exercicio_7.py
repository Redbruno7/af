# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 7: FAÇA UM ALGORITMO PARA LER A BASE E A ALTURA DE UM TRIÂNGULO. 
# EM SEGUIDA, ESCREVA A ÁREA DO MESMO.

import os


os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 7')
print('='*50)

# Entrada
base = float(input('Digite a base do triângulo em centímetros: '))
altura = float(input('Digite a altura do triângulo em centímetros: '))

# Processamento
area_triangulo = (base * altura) / 2

# Saída
print('.'*50)
print(f'A área deste triângulo é: {area_triangulo} cm²')
print('='*50)