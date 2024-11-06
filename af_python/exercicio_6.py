# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 6: FAÇA UM ALGORITMO QUE LEIA A DESCRIÇÃO DO PRODUTO, QUANTIDADE EM ESTOQUE E VALOR UNITÁRIO DO PRODUTO. 
# INFORME O VALOR TOTAL EM PRODUTOS EXISTENTE NO ESTOQUE.

import os


os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 6')
print('='*50)

# Entrada
produto = input('Produto: ')
estoque = int(input('Quantidade em estoque: '))
valor_unidade = float(input('Valor unitário em reais: '))

# Processamento
valor_total = estoque * valor_unidade

# Saída
print('.'*50)
print(f'O valor total de {produto} em estoque é: R${valor_total:.2f}')
print('='*50)