# Herança P/1

class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie
    
    def apresentar(self):
        print(f'Eu sou o(a) {self.especie} chamado(a) {self.nome} e sou da cor {self.cor}')

class Gato(Animal):
    def emitir_som(self):
        print('Miau!')

    def arranhar(self):
        print('O gato está arranhando \n')

class Cachorro(Animal):
    def emitir_som(self):
        print('Au Au Au...\n')

class Elefante(Animal):
    def emitir_som(self):
        print('Pruuuuu...')

gato1 = Gato('Felix', 'Branca', 'Siamese')
gato1.apresentar()
gato1.emitir_som()
gato1.arranhar()

cachorro1 = Cachorro('Thor', 'Preto', 'Pinscher')
cachorro1.apresentar()
cachorro1.emitir_som()
cachorro2 = Cachorro('Rock', 'Branca', 'Pastor Alemão')
cachorro2.apresentar()
cachorro2.emitir_som()

elefante1 = Elefante('Fred', 'Cinza', 'Elefante Asiático')
elefante1.apresentar()
elefante1.emitir_som()
