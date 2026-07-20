#nome = (input('Digite seu nome: '))
#idade = (input('Digite a sua idade: '))

#print(f'Olá {nome}, você tem {idade} anos!')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print(f'A sua média final foi {media:.1f}!')
if media >= 7:
    print('Você foi aprovado!')
elif media >= 5:
    print('Você está de recuperação')
else:
    print('Você foi reprovado...')    