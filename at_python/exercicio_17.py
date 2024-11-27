# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# Faça um programa que receba a idade e o sexo de sete pessoas e que calcule e mostre:
# 1 - A idade média do grupo;
# 2 - A idade média das mulheres;
# 3 - A idade média dos homens.


import os


os.system('cls')

# Título
print('=' * 70)
print('EXERCÍCIO 17 - MÉDIA DE IDADE - MASCULINO E FEMININO')
print('=' * 70)
print()

# Flag
soma_idade = 0
soma_masculino = 0
soma_feminino = 0

# Listas
masculino = []
feminino = []

# Iteração 7 pessoas
for i in range (1, 8):

    # Condição para idade
    while True:
        print('-' * 70)
        idade = int(input(f'Digite a idade da {i}ª pessoa: '))
        if idade < 0:
            print('-' * 70)
            print('Idade inválida. Tente novamente.')
        else:
            break
    
    # Condição gênero
    while True:
        print('-' * 70)
        genero = input(f'Digite o gênero da {i} pessoa (m/f): ').strip().lower()
        if genero == 'm':
            masculino.append(idade)
            print('-' * 70)
            break
        elif genero == 'f':
            feminino.append(idade)
            print('-' * 70)
            break
        else:
            print('-' * 70)
            print('Gênero inválido. '
                  'Digite "m" para masculino ou "f" para feminino')
            
    # Soma idade total
    soma_idade += idade
    print()

# Média idade total
media_total = soma_idade / 7

# Média idade homens
for j in masculino:
    soma_masculino += j
media_m = soma_masculino / len(masculino)

# Média idade mulheres
for k in feminino:
    soma_feminino += k
media_f = soma_feminino / len(feminino)

# Saída
print('=' * 70)
print(f'A média das idades do grupo inteiro é: {media_total:.0f}')
print('-' * 70)
print(f'A média das idades dos homens é: {media_m:.0f}')
print('-' * 70)
print(f'A média das idades das mulheres é: {media_f:.0f}')
print('=' * 70)
print()