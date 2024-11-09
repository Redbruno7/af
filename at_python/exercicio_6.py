# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('='*70)
print('EXERCÍCIO 6 - SIMULAÇÃO DE LUCRO')
print('='*70)

# Entrada
valor = 5.00
ingresso = 120
despesa = 200
reducao_valor = 0.5
aumento_ingresso = 26

# Contador
lucro_maximo = 0
valor_maximo = 0
ingresso_maximo = 0

# Cabeçalho da tabela
print()
print('='*70)
print('TABELA DE SIMULAÇÃO DE LUCRO')
print('='*70)
print(f"| {'Preço do ingresso':<25}| {'Quantidade Vendida':<25}| {'Lucro':<13}|")
print('='*70)

# Iteração de R$5,00 a R$1,00
while valor >= 1.00:
    receita = valor * ingresso
    lucro = receita - despesa
    print(f'| R${valor:<23.2f}| {ingresso:<25}| {lucro:<13.2f}|')
    
    # Cálculo dos válores máximos
    if lucro > lucro_maximo:
        lucro_maximo = lucro
        valor_maximo = valor
        ingresso_maximo = ingresso

    # Cálculo proporcional para iteração
    valor -= reducao_valor
    ingresso += aumento_ingresso
print('=' * 70)

# Saída
print()
print('=' * 70)
print(f'Caso de lucro máximo:')
print('-' * 70)
print(f'Preço do ingresso: R${valor_maximo:.2f}')
print(f'Quantidade de ingressos vendidos: {ingresso_maximo}')
print(f'Lucro: R${lucro_maximo:.2f}')
print('=' * 70)