# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 6: Uma companhia de teatro deseja dar uma série de espetáculos. 
# A direção calcula que a R$5,00 o ingresso, serão vendidos 120 ingressos, e que as despesas serão R$200,00. 
# Diminuindo-se R$0,50 o preço dos ingressos espera-se que as vendas aumentem em 26 ingressos.
# Faça um programa que escreva uma tabela de valores de lucros esperados em função do preço do ingresso, 
# fazendo-se variar esse preço de R$5,00 a R$1,00 de R$0,50 em R$0,50. 
# Escreva, ainda, o lucro máximo esperado, o preço do ingresso e a quantidade de ingressos vendidos para a obtenção desse lucro.

import os


os.system('cls')

# Título
print('='*70)
print('EXERCÍCIO 6')
print('='*70)

# Entrada
valor = 5.00
ingresso = 120
despesa = 200
reducao_valor = 0.5
aumento_ingresso = 26

lucro_maximo = 0
valor_maximo = 0
ingresso_maximo = 0

# Cabeçalho da tabela
print(f"{'Preço do ingresso':<25}{'Quantidade Vendida':<25}{'Lucro':<25}")
print('-'*70)

# Processamento
while valor >= 1.00: # Loop para cálculo de lucro no intervalo de 5.00 a 1.00
    receita = valor * ingresso
    lucro = receita - despesa
    print(f'R${valor:<23.2f}{ingresso:<25}{lucro:<13.2f}')
    
    if lucro > lucro_maximo:
        lucro_maximo = lucro
        valor_maximo = valor
        ingresso_maximo = ingresso

    valor -= reducao_valor
    ingresso += aumento_ingresso

# Saída
print('-'*70)
print(f'Caso de lucro máximo:')
print(f'Preço do ingresso: R${valor_maximo:.2f}')
print(f'Quantidade de ingressos vendidos: {ingresso_maximo}')
print(f'Lucro: R${lucro_maximo:.2f}')
print('='*70)