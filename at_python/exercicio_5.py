# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 5: UMA LOJA TEM 15 CLIENTES CADASTRADOS E DESEJA ENVIAR UMA CORRESPONDÊNCIA A CADA UM DELES ANUNCIANDO UM BÔNUS ESPECIAL. 
# FAÇA UM PROGRAMA QUE LEIA O NOME DO CLIENTE E O VALOR DE SUAS COMPRAS NO ANO PASSADO. 
# CALCULE E MOSTRE UM BÔNUS DE 10% SE O VALOR DAS COMPRAS FOR MENOR QUE R$1.000,00 E DE 15%, CASO CONTRÁRIO.

import os


os.system('cls')

# Título
print('='*70)
print('EXERCÍCIO 5')
print('='*70)

# Entrada
num_clientes = 15

# Processamento e saída
for i in range(1, num_clientes + 1):
    print(f'Cliente {i}:')
    nome = input('Digite o nome do cliente: ')
    valor_compras = float(input('Valor total em compras no ano passado: '))
    if valor_compras < 1000:
        bonus = valor_compras * 0.1
    else:
        bonus = valor_compras * 0.15
    print('.'*70)
    print(f'Cliente: {nome}')
    print(f'Valor em compras no ano passado: R${valor_compras:.2f}')
    print(f'Bônus especial: R${bonus:.2f}')
    print('-'*70)
print('='*70)
teste