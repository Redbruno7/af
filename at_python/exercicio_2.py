# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('='*70)
print('EXERCÍCIO 2')
print('='*70)

# Entrada
numero = int(input('Digite um número inteiro para cálculo: '))

# Processamento e Saída
print('.'*70)
if numero <= 0:
    print('O valor deve ser inteiro e positivo!')
else:
    soma = 0
    for i in range(1, numero + 1):
        soma += 1 / i
    print(f'A soma proposta pelo exercício resulta em: {soma:.2f}')
print('='*70)