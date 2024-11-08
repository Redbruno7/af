# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 70)
print('EXERCÍCIO 3 - PRODUTO DOS NÚMEROS PRIMOS NO INTERVALO ENTRE 92 E 1478')
print('=' * 70)

# Contador
produto = 1 

# Iteração entre 92 e 1478
for numero in range(92, 1479):
    primo = True

    # Validação de número primo entre o intervalo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False 
            break

    # Multiplicação dos números primos
    if primo: 
        produto *= numero

# Saída
print()
print('=' * 70)
print('Cálculo do produto dos números primos entre 92 e 1478:')
print('-' * 70)
print(f'Resultado: {produto}')
print('=' * 70)