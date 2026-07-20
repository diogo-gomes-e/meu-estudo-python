#FUNÇÕES -> def = define

#def saudacao(nome, idade):
#    print(f'Olá {nome}! Você tem {idade} anos de idade')
#
#saudacao('Andre', 35)

#def somar(num1, num2):
#    return num1 + num2

#total = somar(4, 5)
#print(f'O resultado da soma é de: {total}')

#PROGRAMA/FUNÇÃO PARA CALCULO DE DESCONTO

def calcular_desconto(preco, porcentagem):
    return preco - (preco * porcentagem / 100)

valor_final = calcular_desconto(1300, 25)
print(f'O valor final com desconto é de R${valor_final:.2f}')