# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE
# EXERCÍCIO 1: FAÇA UM ALGORITMO PARA LER E EM SEGUIDA EXIBIR AS SEGUINTES INFORMAÇÕES DE UMA PESSOA: 
# NOME, IDADE, SEXO, PESO, ALTURA, PROFISSÃO, RUA, BAIRRO, CIDADE, ESTADO, CEP, TELEFONE

import os
import datetime

os.system('cls')

# Título
print('='*50)
print('EXERCÍCIO 1')
print('='*50)

# Entrada
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
genero = input('Digite seu gênero (Masculino/Feminino): ')
peso = float(input('Digite seu peso em quilo: '))
altura = float(input('Digite sua altura em metro: '))
profissao = input('Digite sua profissão: ')
rua = input('Digite o nome da sua rua: ')
bairro = input('Digite o nome do seu bairro: ')
cidade = input('Digite o nome da sua cidade: ')
estado = input('Digite o nome do seu estado: ')
cep = input('Digite seu CEP: ')
telefone = input('Digite seu número de telefone: ')
print('-'*50)

# Saída
print(f'Informações Fornecidas:')
print('-'*50)
print(f'Nome........: {nome}')
print(f'Idade.......: {idade} anos')
print(f'Gênero......: {genero}')
print(f'Peso........: {peso:.2f} kg')
print(f'Altura......: {altura:.2f} m')
print(f'Profissao...: {profissao}')
print(f'Rua.........: {rua}')
print(f'Bairro......: {bairro}')
print(f'Cidade......: {cidade}')
print(f'Estado......: {estado}')
print(f'CEP.........: {cep}')
print(f'Telefone....: {telefone}')
print('='*50)