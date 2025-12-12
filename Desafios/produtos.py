# Crie um programa que pergunte ao funcionário qual produto o cliente comprou de acordo com o valor inserido pelo funcionario
# onde terá o valor de cada produto, o programa deve fazer a soma dos produtos e retornar o valor total da venda
# após isso o programa deve perguntar ao funcionário se o mesmo deseja aplicar % de desconto sobre o valor total 
# e retornar o valor total atualizado da venda, após isso deve-se perguntar qual a forma de pagamento, se for pix ou dinheiro (desconto aplicável)
# agora, se for cartão de débito ou crédito (desconto não aplicável)

usuario_escolhendo = 's'
valor_compra = 0
adicional = 0
quant_desconto = 0
pagamento_desconto = ['pix', 'dinheiro']

def calcular_porcentagem(parte, total):
    return total * (parte / 100)

produtos = {'vestido' : 100,
            'saia' : 50,
            'calça' : 90,
            'oculos' : 100 }

print('Bem vindo a loja de roupas!\n') 
print('Qual peça você comprou?\n') 
print('1 - Vestido\n')
print('2 - Saia\n')
print('3 - Calça\n')
print('4 - Óculos\n')

    
while usuario_escolhendo == 's':

    usuario = int(input('Qual produto você comprou? Digite o numero do item no menu:\n'))
    if usuario == 1:
        adicional = produtos['vestido']
    elif usuario == 2:
        adicional = produtos['saia']
    elif usuario == 3:
        adicional = produtos['calça']
    elif usuario == 4:
        adicional = produtos['oculos']
    elif usuario not in (1, 2, 3, 4):
        print('Produto inválido!')

    valor_compra = valor_compra + adicional

    usuario_escolhendo = input('Deseja comprar mais alguma coisa? Digite s para sim e n para não:')
    usuario_escolhendo.lower()

    if usuario_escolhendo == 'n':
        break
    
print(f'O valor total da conta é de R${valor_compra}')

quer_desconto = input('Funcionario, voce quer aplicar desconto? s para sim e n para não:\n')
quer_desconto.lower()

if quer_desconto == 's':
    quant_desconto = int(input('Quanto de desconto quer aplicar:\n'))
    valor_desconto = calcular_porcentagem(quant_desconto, valor_compra)

    valor_atualizado = valor_compra - valor_desconto

    pagamento = input('Qual a forma de pagamento? Pix, dinheiro ou cartão?')
    pagamento.lower()
    if pagamento in pagamento_desconto:
        print(f'O valor da sua compra com desconto é de {valor_atualizado}')
    elif pagamento not in pagamento_desconto:
        print(f'Desconto somente aplicável em pagamento com pix ou dinheiro. Seu total é de {valor_compra}')
if quer_desconto != 's':
    pagamento = input('Qual a forma de pagamento? Pix, dinheiro ou cartão?')
    pagamento.lower()
    print(f'O valor da compra com pagamento no {pagamento} é de R$ {valor_compra}')



