# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 50)
print('EXERCÍCIO 5 - CÁLCULO DE BÔNUS')
print('=' * 70)

# Lista
lista_clientes = []

# Contador
num_clientes = 3

# Iteração entre 15 clientes
for i in range(1, num_clientes + 1):
    print()
    print('=' * 70)
    print(f'Cliente {i}:')
    print('=' * 70)

    # Entrada nome
    nome = input('Digite o nome do cliente: ')
    print('-' * 70)

    # Validação de valor de compra
    while True:
        valor_compra = float(input('Valor total em compras no ano passado: '))
        print('=' * 70)

        if valor_compra > 0:
            break
        else: 
            print('Valor inválido! Digite um valor positivo.')
            print('-' * 70)

    # Cálculo bônus
    if valor_compra < 1000:
        bonus = valor_compra * 0.1
    else:
        bonus = valor_compra * 0.15
    
    # Armazenamento na lista
    lista_clientes.append(
        {'nome': nome, 'valor_compra': valor_compra, 'bonus': bonus}
        )

# Saída
print()
print('='*70)
print('RELATÓRIO')

for cliente in lista_clientes:
    print('='*70)
    print(f'Cliente: {cliente['nome']}')
    print(f'Valor em compras no ano passado: R${cliente['valor_compra']:.2f}')
    print(f'Bônus especial: R${cliente['bonus']:.2f}')

print('='*70)