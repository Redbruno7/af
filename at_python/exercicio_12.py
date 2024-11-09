# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 70)
print('EXERCÍCIO 12 - ANÁLISE DE IDADE, ALTURA E PESO')
print('=' * 70)

# Entrada contadores
total_pessoas = 25
contador_idade = 0
soma_altura = 0
contador_altura = 0
contador_peso = 0

# Iteração de 25 pessoas
for i in range(1, total_pessoas + 1):
    print()
    print('=' * 70)
    print(f'Dados da pessoa {i}: ')
    print('=' * 70)
    print ()
    
    # Validação de idade
    while True:
        
        print('-' * 70)
        idade = int(input('Digite a idade: '))
        print('-' * 70)
        if idade >= 0:
            break
        else:
            print('Idade inválida! Digite um valor positivo.')

    # Validação de altura
    while True:
        altura = float(input('Digite a altura em metros: '))
        print('-' * 70)
        if altura > 0:
            break
        else:
            print('Altura inválida! Digite um valor positivo.')
            print('-' * 70)
    
    # Validação de peso
    while True:
        peso = float(input('Digite o peso em quilos: '))
        print('-' * 70)
        if peso > 0:
            break
        else:
            print('Peso inválido! Digite um valor positivo.')
            print('-' * 70)
    
    # Contagem de pessoas com idade > 50 anos
    if idade > 50:
        contador_idade += 1
    
    # Soma da altura de pessoas entre 10 e 20 anos
    if 10 <= idade <= 20:
        soma_altura += altura
        contador_altura += 1

    # Contagem de pessoas com peso < 40 kg
    if peso < 40:
        contador_peso += 1

# Cálculo média de altura de pessoas entre 10 e 20 anos
if contador_altura > 0:
    media_altura = soma_altura / contador_altura
else:
    media_altura = 0

# Percentual de pessoas com peso < 40 kg
percentual_peso = (contador_peso / total_pessoas) * 100

# Saída
print()
print('=' * 70)
print(f'Quantidade de pessoas com idade superior a 50 anos: {contador_idade}')
print('-' * 70)
print('Média de altura das pessoas com idade entre 10 e 20 anos: '
      f'{media_altura:.2f} m')
print('-' * 70)
print('Percentual de pessoas com peso inferior a 40 kg: '
      f'{percentual_peso:.2f}%')
print('=' * 70)