import random
import string
import os
import sys

def gerar_senha(tamanho):
    caractere = string.ascii_letters + string.digits + string.punctuation

    senha = ''.join(random.choice(caractere) for i in range(tamanho))

    return senha

def main():
    tamanho = int(input(f'Digite o tamanho da senha desejada:\n'))

    senha = gerar_senha(tamanho)
    print(f'Senha gerada: {senha}')

if __name__ == '__main__':

    nova_senha = 's'

    while nova_senha == 's':

        main()

        nova_senha = input(f'Deseja gerar uma nova senha? s para sim e n para não:\n')
        nova_senha.lower()

        if nova_senha != 's':
            sys.exit()

        os.system('cls')
            
