# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 4: FAÇA UM ALGORITMO QUE SOLICITE A IDADE E O NOME DE QUATRO PESSOAS. 
# CALCULE E IMPRIMA A MÉDIA ARITMÉTICA DAS IDADES.

import os


os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 4')
print('='*50)

# Entrada
nome_1 = input('1º Nome: ')
idade_1 = int(input('1ª Idade: '))
nome_2 = input('2º Nome: ')
idade_2 = int(input('2ª Idade: '))
nome_3 = input('3º Nome: ')
idade_3 = int(input('3ª Idade: '))
nome_4 = input('4º Nome: ')
idade_4 = int(input('4ª Idade: '))

# Processamento
media = (idade_1 + idade_2 + idade_3 + idade_4) / 4

# Saída
print('.'*50)
print(f'A média aritmética das idades de {nome_1}, {nome_2}, '
      f'{nome_3} e {nome_4} é: {media:.0f}.')
print('='*50)