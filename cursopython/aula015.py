# Herança múltipla e Herança de Multinível 

# Classe Avô

class Animal:
    def __init__(self, nome):
        self.nome = nome

# Classes Pai
class Predador(Animal):
    def cacando(self):
        print(f'O animal {self.nome} está caçando!')

class Presa(Animal):
    def fugindo(self):
        print(f'O animal {self.nome} está sendo caçado!')

# Classes Filho

class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Predador, Presa):
    pass

class Gato(Predador, Presa):
    pass

class Rato (Presa):
    pass

coelho1 = Coelho('Theo')
tigre1 = Tigre('Leo')
golfinho1 = Golfinho('Billy')
gato1 = Gato('Cleiton')
rato1 = Rato('Josefino')

coelho1.fugindo()
tigre1.cacando()
golfinho1.cacando()
gato1.cacando()
rato1.fugindo()