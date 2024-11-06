# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 2: FAÇA UM ALGORITMO QUE INFORME O NOME E IDADE DE DUAS PESSOAS. 
# MOSTRE O NOME E IDADE DAS DUAS PESSOAS NA TELA.

import os


os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 2')
print('='*50)

# Entrada
nome_1 = input('Digite o primeiro nome: ')
idade_1 = int(input('Digite a primeira idade: '))
nome_2 = input('Digite o segundo nome: ')
idade_2 = int(input('Digite a segunda idade: '))

# Saída
print('.'*50)
print(f'{nome_1} tem {idade_1} anos.')
print(f'Enquanto {nome_2} tem {idade_2} anos.')
print('='*50)