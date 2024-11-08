# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('='*70)
print('EXERCÍCIO 15 - VERIFICAÇÃO DE NÚMEROS ENTRE 30 E 90')
print('='*70)

# Entrada contador
contador = 0
total_numeros = 10

# Oteração de 10 números
for i in range(1, total_numeros + 1):
    print()
    print('='*70)
    numero = float(input(f'Digite o {i}º número: '))
    print('='*70)

    # Condição 1: nº entre 30 e 90
    if 30 <= numero <= 90:
        contador += 1

# Saída
print()
print('='*70)
print(f'Quantidade de números entre 30 e 90: {contador}')
print('='*70)