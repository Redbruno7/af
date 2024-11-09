# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 40)
print('EXERCÍCIO 10 - TABUADA de 1 a 10')
print('=' * 40)
print()

# Iteração entre os números 1 a 10
for numero in range(1, 11):
    print('=' * 40)
    print(f'Tabuada de {numero}:')
    
    # Iteração dos números multiplicados
    for i in range(1,11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
print('=' * 40)