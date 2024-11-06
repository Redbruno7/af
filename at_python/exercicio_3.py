# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 3: FAÇA UM PROGRAMA QUE CALCULE E MOSTRE O PRODUTO DOS NÚMEROS PRIMOS ENTRE 92 E 1.478.

import os


os.system('cls')

# Título
print('='*70)
print('EXERCÍCIO 3')
print('='*70)

# Entrada
numero = int

# Processamento e Saída # INCOMPLETO
print('Cálculo do produto dos números primos entre 92 e 1478:')
print('.'*70)
produto = 92
for numero in range(92, 1479):
    for i in range(92, produto + 1):
        if (numero % numero == 0) and (numero % 1 == 0) and (numero % i != 0):
            produto *= numero
print(f'O resultado é: {produto}')
print('='*70)