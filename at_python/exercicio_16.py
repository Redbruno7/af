# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# Faça um programa que receba dez idades, pesos e alturas e que calcule e mostre:
# 1 - A média das idades das dez pessoas;
# 2 - A quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50m;
# 3 - A percentagem de pessoas com idade entre 10 e 30 anos entre as pessoas medem mais de 1,90m.


import os


os.system('cls')

# Título
print('=' * 90)
print('EXERCÍCIO 16 - ANÁLISE E CÁLCULO DE MÉDIA DE ATRIBUTOS FÍSICOS')
print('=' * 90)
print()

# Flag
soma_alturas = 0
contador_2 = 0
contador_3 = 0

# Entrada
for i in range(1, 11):

    # Condição idade
    while True:
        print('-' * 90)
        idade = int(input(f'Digite a idade da {i}ª pessoa: '))

        if idade < 0:
            print('-' * 90)
            print('Idade inválida. Tente novamente.')
        else:
            break

    # Condição peso
    while True:
        print('-' * 90)
        peso = float(input(f'Digite o peso da {i}ª pessoa: '))
        
        if peso < 0:
            print('-' * 90)
            print('Peso inválido. Tente novamente.')
        else:
            break

    # Condição altura
    while True:
        print('-' * 90)
        altura = float(input(f'Digite a altura da {i}ª pessoa: '))

        if altura < 0:
            print('-' * 90)
            print('Altura inválida. Tente novamente.')
        else:
            print('-' * 90)
            print()
            break

    # Soma das alturas
    soma_alturas += altura

    # Condição (i > 90 kg) e (i < 1.50 m)
    if (peso > 90) and (altura < 1.50):
        contador_2 += 1

    # Condição (10 anos <= i <= 30 anos) e (pessoa > 1.90 m)
    if (idade >= 10) and (idade <= 30) and (altura > 1.90):
        contador_3 += 1

# Média das alturas
media_altura = soma_alturas / 10

# Saída
print('=' * 90)
print(f'A média das alturas é: {media_altura:.2f} m')
print('-' * 90)
print('Quantidade de pessoas com peso maior '
      f'que 90 quilos e altura menor que 1,50 m: {contador_2}')
print('-' * 90)
print('Percentual de pessoas com idades entre 10 e 30 anos que medem mais '
      f'que 1,90 m: {contador_3}')
print('=' * 90)
print()