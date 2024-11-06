# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 5: FAÇA UM ALGORITMO PARA LER DOIS INTEIROS (VARIÁVEIS A E B) 
# E IMPRIMIR O RESULTADO DO QUADRADO DA DIFERENÇA DO PRIMEIRO VALOR PELO SEGUNDO.

import os


os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 5')
print('='*50)

# Entrada
a = int(input('1º Valor: '))
b = int(input('2º Valor: '))

# Processamento
x = (a - b) ** 2

# Saída
print('.'*50)
print(f'O quadrado da diferença do primeiro valor pelo segundo é: {x}')
print('='*50)