# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 80)
print('EXERCÍCIO 14 - ANÁLISE DE ATRIBUTOS FÍSICOS')
print('=' * 80)

# Entrada contadores
idade_peso = 0
soma_idade = 0
altura_baixa = 0
olho_azul = 0
ruivo_sem_azul = 0
total_pessoas = 3

# Iteração para 20 pessoas
for i in range(1, total_pessoas + 1):
    print()
    print('=' * 80)
    print(f'Dados da pessoa {i}:')
    print('=' * 80)

    # Validação idade
    while True:
        idade = int(input('Digite a idade: '))
        print('-' * 80)
        if idade >= 0:
            break
        else:
            print('Idade inválida! Digite um valor positivo.')
            print('-' * 80)
    
    # Validação peso
    while True:
        peso = float(input('Digite o peso em quilos: '))
        print('-' * 80)
        if peso > 0:
            break
        else:
            print('Peso inválido! Digite um valor positivo.')
            print('-' * 80)
    
    # Validação altura
    while True:
        altura = float(input('Digite a altura em metros: '))
        print('-' * 80)
        if altura > 0:
            break
        else:
            print('Altura inválida! Digite um valor positivo.')
            print('-' * 80)

    # Validação cor olho
    while True:
        cor_olho = input('Digite a cor dos olhos '
                    '(A - azul, P - Preto, V - Verde, C- Castanho): ').upper()
        print('-' * 80)
        if cor_olho in ['A', 'P', 'V', 'C']:
            break
        else:
            print('Cor inválida! Digite um dos códigos indicados para cor.')
            print('-' * 80)

    # Validação cor  cabelo
    while True:
        cor_cabelo = input('Digite a cor do cabelo '
                '(P - Preto, C - Castanho, L - Louro, R - Ruivo): ').upper()
        if cor_cabelo in ['P', 'C', 'L', 'R']:
            break
        else:
            print('-' * 80)
            print('Cor inválida! Insira um dos códigos indicados para cor.')
            print('-' * 80)
    # Condição 1: Nº pessoas > 50 anos e peso < 60 kg
    if (idade > 50) and (peso < 60):
        idade_peso += 1

    # Condição 2: Soma das idades de pessoas com altura < 1.50 m
    if altura < 1.50:
        soma_idade += idade
        altura_baixa += 1

    # Condição 3: Contagem de pessoas com olhos azuis
    if cor_olho == 'A':
        olho_azul += 1

    # Condição 4: Pessoas ruivas que não têm olhos azuis
    if (cor_cabelo == 'R') and (cor_olho != 'A'):
        ruivo_sem_azul += 1

    print('=' * 80)
# Média de idade para pessoas < 1.50 m
if altura_baixa > 0:
    media_altura_baixa = soma_idade / altura_baixa
else:
    media_altura_baixa = 0

# Percentual de pessoas com olhos azuis
percentual_azul = (olho_azul / total_pessoas) * 100

# Saída
print()
print('=' * 80)
print('Resultados:')
print('=' * 80)
print('Quantidade de pessoas com idade > 50 anos e peso < 60 kg: '
      f'{idade_peso}')
print('-' * 80)
print('Média das idades das pessoas com altura < 1.50 m: '
      f'{media_altura_baixa}')
print('-' * 80)
print(f'Percentual de pessoas com olhos azuis: {percentual_azul:.2f}%')
print('-' * 80)
print(f'Quantidade de pessoas ruivas sem olhos azuis: {ruivo_sem_azul}')
print('=' * 80)