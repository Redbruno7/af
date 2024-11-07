# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 3: FAÇA UM PROGRAMA QUE CALCULE E MOSTRE O PRODUTO DOS NÚMEROS PRIMOS ENTRE 92 E 1.478.

import os


os.system('cls')

# Título
print('='*70)
print('EXERCÍCIO 3')
print('='*70)

# Inicialização da variável do produto
produto = 1 # Variável para armazenar o produto dos números primos

# Processamento: Iteração dos números no intervalo
for numero in range(92, 1479): # Itera de 92 a 1478
    primo = True # Assume que número é primo

    # Validação de número primo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0: # Se a divisão for exata (resto 0), o número não é primo
            primo = False 
            break # Sai do loop porque encontrou um divisor

    # Multiplica apenas se o número for primo
    if primo: 
        produto *= numero # Acumula o produto dos números primos no intervalo

# Saída
print('Cálculo do produto dos números primos entre 92 e 1478:')
print('.'*70)
print(f'Resultado: {produto}')
print('='*70)