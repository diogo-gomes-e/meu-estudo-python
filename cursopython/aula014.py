# Herança p/2 

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos de idade!')

class Funcionario(Pessoa):
    def __init__ (self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def trabalhar(self):
        print(f'{self.nome} está trabalhando como {self.cargo}.')

class Cliente(Pessoa):
    def __init__ (self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo

    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'A sua compra de R${valor_compra} foi aprovada! Seu saldo atual é de: R${self.saldo}!')
        else:
            print(f'Saldo insuficiente!')

f1 = Funcionario('João', 24, 'Gerente de contas')
f1.apresentar()
f1.trabalhar()

f2 = Funcionario('Pedro', 37, 'Dev Junior')
f2.apresentar()
f2.trabalhar()

c1 = Cliente('Arthur', 16, 300)
c1.apresentar()
c1.comprar(350)

c2 = Cliente('Jose', 27, 500)
c2.apresentar()
c2.comprar(200)
