#validação login

#usuario = input('Digite o seu usuário: ')
#senha = input('Digite a sua senha: ')

#login_validado = usuario == 'Admin' and senha == 'DuduChupingole123'

#print(f'Login permitido: {login_validado}')

# CONVERSOR DE UNIDADES 

#metro = float(input('Quantos metros você quer transformar em centímetros? '))
#centimetros = metro * 100

#print(f'Transformando {metro} em centímetros você terá {centimetros:.00f} centímetros!')

#VERIFICAÇÃO ACESSO A PEPSI

idade = int(input('Qual é a sua idade ? '))
autorizacao_pais = (input('Você tem autorização dos pais? (s/n): '))
six = (input('Você é estudante com parceria da Six? (s/n?): '))

if idade >= 18:
    print('Acesso liberado.')
elif idade >= 16 and autorizacao_pais == 's':
    print('Acesso liberado via autorização.')
elif autorizacao_pais == 's' and six == 's':
    print('Acesso liberado via parceria Six.')
else:
    print('Acesso negado.')

