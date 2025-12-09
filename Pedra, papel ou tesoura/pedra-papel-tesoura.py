# Criar um jogo de pedra papel ou tesoura entre o usuário e a máquina
import random

novo_jogo = 's'

def jogo():

    computador = random.choice(['pedra', 'papel', 'tesoura'])

    usuario = input('Digite o que deseja escolher para jogar: Pedra, papel ou tesoura?\n')
    usuario = usuario.lower()

    if usuario == computador:
        print(f'Empate! Você jogou {usuario} e o computador também jogou {computador}')
    elif usuario != 'papel' and computador == 'pedra':
        print(f'Você perdeu! O computador jogou {computador}, e {computador} ganha de {usuario}')
    elif usuario != 'pedra' and computador == 'tesoura': 
        print(f'Você perdeu! O computador jogou {computador}, e {computador} ganha de {usuario}')
    elif usuario != 'tesoura' and computador == 'papel':
        print(f'Você perdeu! O computador jogou {computador}, e {computador} ganha de {usuario}')
    else: 
        print(f'Parabéns, você ganhou! {usuario} ganha de {computador}')


while novo_jogo == 's':
    
    jogo()

    novo_jogo = input('Deseja jogar novamente? Digite "s" para sim e "n" para não.\n')
    novo_jogo.lower
    novo_jogo

# Tarefa: adicionar tratamento de exceções