# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 8: CONSTRUA UM ALGORITMO PARA CALCULAR AS RAÍZES DE UMA EQUAÇÃO DO 2º GRAU, 
# SENDO QUE OS VALORES A, B E C SÃO FORNECIDOS PELO USUÁRIO.

import os


os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 8')
print('='*50)

# Entrada
a = float(input('Digite o valor de "a": '))
b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))

# Processamento
delta = (b ** 2) - (4 * a * c)
raiz_delta = delta ** (1 / 2)
raiz_1 = (- b + raiz_delta) / (2 * a)
raiz_2 = (- b - raiz_delta) / (2 * a)

# Saída
print('.'*50)
print(f'As raízes da equação proposta são: {raiz_1:.2f} e {raiz_2:.2f}')
print('='*50)