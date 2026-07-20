#from funcoes import saudacao, soma

#saudacao('Pedro')
#print(soma(2, 15))

#import funcoes

#funcoes.saudacao('Andre')
#print(funcoes.soma(2, 23))

from funcoes import verificar_maioridade

minha_idade = int(input('Digite a sua idade: '))

if verificar_maioridade(minha_idade):
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')