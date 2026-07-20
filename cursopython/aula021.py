# Nested Classes

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motores = []

    # A classe Motor está ANINHADA (Nested) dentro de Carro
    class Motor:
        def __init__(self, marca, potencia):
            self.marca = marca
            self.potencia = potencia

        def exibir_detalhes(self):
            return f"Marca: {self.marca} | {self.potencia} cv"

    # Método para criar e adicionar o motor diretamente de dentro do Carro
    def adicionar_motor(self, marca, potencia):
        # Como Motor está dentro de Carro, instanciamos usando self.Motor
        novo_motor = self.Motor(marca, potencia)
        self.motores.append(novo_motor)

    def listar_motores(self):
        print(f"Motores disponíveis para o {self.modelo}:")
        for motor in self.motores:
            # Chamamos o método da nossa classe interna
            print(f"- {motor.exibir_detalhes()}")

# Criando o carro
meu_carro = Carro("Mustang")

# Agora adicionamos os motores passando apenas os dados. 
# O próprio carro se encarrega de criar os objetos de Motor internamente!
meu_carro.adicionar_motor('Ford', 300)
meu_carro.adicionar_motor('Ferrari', 650)

# Listando os motores do carro
meu_carro.listar_motores()