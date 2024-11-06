# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 3: FAÇA UM ALGORITMO QUE DIGITE O NOME E IDADE DE DUAS PESSOAS. 
# ENCONTRE E IMPRIMA A DIFERENÇAS DE IDADES ENTRE AS PESSOAS. 
# E A SOMA DAS IDADES DAS PESSOAS.

import os


os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 3')
print('='*50)

# Entrada
nome_1 = input('Digite o primeiro nome: ')
idade_1 = int(input('Digite a primera idade: '))
nome_2 = input('Digite o segundo nome: ')
idade_2 = int(input('Digite a segunda idade: '))

# Processamento
print('.'*50)
if idade_1 > idade_2:
    diferenca_1 = idade_1 - idade_2
    print(f'A diferença de idade entre {nome_1} e {nome_2} é: '
          f'{diferenca_1} anos.')
elif idade_1 == idade_2:
    print(f'Os dois tem a mesma idade, portanto não há diferença.')
else:
    diferenca_2 = idade_2 - idade_1
    print(f'A diferença de idade entre {nome_2} e {nome_1} é: '
          f'{diferenca_2} anos.')
soma = idade_1 + idade_2
print(f'Enquanto a soma das idades é: {soma} anos.')