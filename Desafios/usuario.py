# Crie um programa que pergunte o nome do usuário, idade, empresa/cargo que trabalha e seu hobby ( o programa deve retornar os dados solicitados em prints)
# Após isso, trate com try, execpt, if/elif/else e finnaly (se aplicável)

import os

novo_usuario = 's'
nome = ''

def usuario():
    global nome, idade, empresa, cargo, hobbie
    nome = input(f'Olá, qual o seu nome?\n')
    idade = int(input(f'Bem vindo(a) {nome}, qual a sua idade?\n'))
    empresa = input(f'Legal, qual a sua empresa?\n')
    cargo = input(f'E qual o seu cargo na empresa {empresa}?\n')
    hobbie = input(f'Quando não esta atuando como {cargo}, qual o seu hobbie?\n')

    

while novo_usuario == 's': 

    try:
        usuario()
    except ValueError:
        print('Não consegui reconhecer o dado, tente novamente!')
    else: 
        print(f'Maravilha {nome}, esses são os dados que tenho de você:\n')
        print(f'Seu nome é {nome} e você tem {idade} anos.\n')
        print(f'Você trabalha na empresa {empresa} como {cargo}.\n')
        print(f'Quando não está trabalhando, seu hobbie é {hobbie}!')

    novo_usuario = input(f'Gostaria de se apresentar novamente?')
    novo_usuario.lower()
    os.system('cls')
    
print(f'Prazer em te conhecer! {nome}')
