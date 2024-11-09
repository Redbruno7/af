# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS 
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 63)
print('EXERCÍCIO 8 - TABELA DE FAIXA ETÁRIA')
print('=' * 63)
print()

# Entrada
total_pessoas = 15

# Contador
faixa_1 = 0
faixa_2 = 0
faixa_3 = 0
faixa_4 = 0
faixa_5 = 0

# Iteração entre 15 pessoas
for i in range(1, 16):
    print('-' * 63)

    # Validação de idade
    while True:
        idade = int(input(f'Digite a idade da {i}ª pessoa: '))
        print('-' * 63)
        if idade >= 0:
            break
        else:
            print(f'Idade inválida!')
            print('-' * 63)
    
    # Classificação nas faixas etárias
    if idade <= 15:
        faixa_1 += 1
    elif (idade > 15) and (idade <= 30):
        faixa_2 += 1
    elif(idade > 30) and (idade <= 45):
        faixa_3 += 1
    elif(idade > 45) and (idade <= 60):
        faixa_4 += 1
    else:
        faixa_5 += 1

    # Percentual de idade primeira e última faixas
    percentual_1 = (faixa_1 / total_pessoas) * 100
    percentual_2 = (faixa_5 / total_pessoas) * 100

# Saída (Tabela)
print()
print('=' * 63)
print(f"{'| FAIXA ETÁRIA':<30}| {'Nº DE PESSOAS':<30}|")
print('-' * 63)
print(f"{'| 1ª Faixa (Até 15 anos)':<30}| {faixa_1:<30}|")
print('-' * 63)
print(f"{'| 2ª Faixa (De 16 a 30 anos)':<30}| {faixa_2:<30}|")
print('-' * 63)
print(f"{'| 3ª Faixa (De 31 a 45 anos)':<30}| {faixa_3:<30}|")
print('-' * 63)
print(f"{'| 4ª Faixa (De 46 a 60 anos)':<30}| {faixa_4:<30}|")
print('-' * 63)
print(f"{'| 5ª Faixa (Acima de 60 anos)':<30}| {faixa_5:<30}|")
print('=' * 63)

# Saída Percentuais
print()
print('=' * 63)
print(f'Percentual da 1ª faixa: {percentual_1:.0f}%')
print(f'Percentual da 5ª faixa: {percentual_2:.0f}%')
print('=' * 63)