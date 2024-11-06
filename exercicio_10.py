# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 10: FAÇA UM ALGORITMO PARA CALCULAR E IMPRIMIR O SALÁRIO BRUTO A SER RECEBIDO POR UM FUNCIONÁRIO EM UM MÊS. 
# VOCÊ DEVERÁ UTILIZAR OS SEGUINTES DADOS: 
# NÚMERO DE HORAS QUE O FUNCIONÁRIO TRABALHOU NO MÊS, 
# VALOR RECEBIDO POR HORA DE TRABALHO, 
# O VALOR DA CONTRIBUIÇÃO AO INSS, 
# NÚMERO DE DEPENDENTES (FILHOS MENORES DE 14 ANOS PARA ADICIONAR O SALÁRIO FAMÍLIA) 
# E O VALOR DO SALÁRIO FAMÍLIA POR Nº DE DEPENDENTES

import os


os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 10')
print('='*50)

# Entrada
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
valor_hora = float(input('Digite o valor da hora de trabalho: '))
valor_inss = int(input('Porcentagem de contribuição ao INSS: '))
dependentes = int(input('Digite o número de dependentes do funcionário: '))
valor_dependente = int(input('Porcentagem adicional por dependente: '))

# Processamento
salario_base = horas_trabalhadas * valor_hora
salario_dependente = salario_base * (valor_dependente / 100)
salario_liquido = salario_base + (salario_dependente * dependentes)
contribuicao_inss = salario_liquido * (valor_inss / 100)
salario_bruto = salario_liquido - contribuicao_inss

# Saída
print('.'*50)
print(f'O salário bruto do funcionário será de: R${salario_bruto:.2f}')
print('='*50)