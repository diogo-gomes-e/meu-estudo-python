#VERIFICAÇÃO DE MOTORISTA

#idade = int(input('Qual é a sua idade? '))
#carteira = (input('Você tem carteira de motorista? (s/n): '))

#if idade >= 18 and carteira == 's':
#    print('Você foi liberado!')
#else:
#    print('Você não foi liberado e será autuado!')

#DESCONTO DE UM PRODUTO

preco = float(input('Digite o valor do produto: '))
desconto = float(input('Digite a porcentagem do desconto a ser aplicado: '))
preco_desconto = preco - (preco * desconto / 100)

print(f'Seu produto tinha valor inicial de R${preco:.1f}, com o desconto aplicado está saindo por R${preco_desconto:.1f}!')
