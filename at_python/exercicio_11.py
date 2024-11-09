# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 70)
print('EXERCÍCIO 11 - CÁLCULO DE COMPRAS')
print('=' * 70)
print()

# Contadores
total_vista = 0.00
total_prazo = 0.0

# Iteração de 15 transações
for i in range(1,16):
    print('=' * 70)
    print(f'Transação {i}: ')
    print('=' * 70)

    # Verificação de inserção do código da compra
    print()
    print('-' * 70)
    while True:
        codigo = input('Digite o código da transação '
                       '(V para vista, P para prazo): ')
        print('-' * 70)
        
        if codigo in ['V', 'v', 'P', 'p']:
            break
        else:
            print(f'Código inválido! Digite V ou P.')
            print('-' * 70)
        
    # Verificação de valor positivo
    while True:
        valor = float(input('Digite o valor da transação: R$ '))
        print('-' * 70)
        
        if valor >= 0:
            break
        else:
            print('Valor inválido! Digite um valor positivo.')
            print('-' * 70)

    # Verificação de transação e acumulação de valores
    if codigo in ['V', 'v']:
        total_vista += valor
    else:
        total_prazo += valor
    
    print()

# Cálculo da primeira prestação
primeira_prestacao = total_prazo / 3

# Saída
print('=' * 70)
print(f'Total das compras à vista: R${total_vista:.2f}')
print('-' * 70)
print(f'Total das compras à prazo: R${total_prazo:.2f}')
print('-' * 70)
print('Valor da primeira prestação se comprada à prazo: '
      f'R${primeira_prestacao:.2f}')
print('=' * 70)