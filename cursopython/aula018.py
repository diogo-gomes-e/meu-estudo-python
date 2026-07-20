# Polymorphism p/2

class Pessoa1:
    def microfone(self):
        print('Meu nome é Pedro.')

class Pessoa2:
    def microfone(self):
        print('Meu nome é Maria.')

class Pessoa3:
    def microfone(self):
        print('Meu nome é Eduardo.')

class Pessoa4:
    def microfone(self):
        print('Meu nome é João.')

sala = [Pessoa1(), Pessoa2(), Pessoa3(), Pessoa4()]

for pessoas in sala:
    pessoas.microfone()