# Exemplos com a função Super()
# Sistema de Escola

class Escola():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status

    def Apresentar(self):
        print(f'Meu nome é {self.nome}.')

    def verfificar_status(self):
        print(f'Status: {"ATIVO" if self.status else "INATIVO"}')

class Aluno(Escola):
    def __init__(self, nome, idade, status, ano):
        super().__init__(nome, idade, status)
        self.ano = ano

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um aluno da escola!')

class Professor(Escola):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um(a) professor(a) da escola!')

class Assistente(Escola):
    def __init__(self, nome, idade, status, bloco):
        super().__init__(nome, idade, status)
        self.bloco = bloco
 
    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um(a) assistente da escola!')

class Diretoria(Escola):
    def __init__(self, nome, idade, status, cargo):
        super().__init__(nome, idade, status)
        self.cargo = cargo

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou {self.cargo} da escola e faço parte da diretoria da escola!')

a1 = Aluno(nome='Pedro', idade=14, status=True, ano=8)
p1 = Professor(nome='Jorge', idade=50, status=True, materia='Português')
as1 = Assistente(nome='Larissa', idade=25, status=False, bloco='Bloco B')
d1 = Diretoria(nome='Pablo', idade=48, status=True, cargo='Vice-Diretor')

a1.Apresentar()
a1.verfificar_status()
p1.Apresentar()
p1.verfificar_status()
as1.Apresentar()
as1.verfificar_status()
d1.Apresentar()
d1.verfificar_status()