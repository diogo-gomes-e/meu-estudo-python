import sqlite3

# Molde do Carro
class Carro:
    def __init__(self, modelo, marca, potencia):
        self.modelo = modelo
        self.marca = marca
        self.potencia = potencia
    
# Conexão com o Banco    
conexao = sqlite3.connect('oficina.db')
cursor = conexao.cursor()

# Criar a tabela se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT,
        marca TEXT,
        potencia INTEGER                   
    )           
''')
conexao.commit()

while True:
    print('\n--- MENU OFICINA ---')
    print('1. Cadastrar novo carro')
    print('2. Listar carros cadastrados')
    print('3. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == "1":
        print('\n[Novo Cadastro ]')
        modelo = input('Digite o modelo: ')
        marca = input('Digite a marca: ')
        potencia = int(input('Digite a potencia (cv): '))
        novo_carro = Carro(modelo, marca, potencia)
        cursor.execute('''
            INSERT INTO carros (modelo, marca, potencia)
            VALUES (?, ?, ?)
        ''', (novo_carro.modelo, novo_carro.marca, novo_carro.potencia))

        conexao.commit()
        print(f"Sucesso! {novo_carro.modelo} cadastrado.")

    elif opcao == "2":
        print("\n[ Lista de Carros no Banco ]")
        cursor.execute("SELECT * FROM carros")
        todos_os_carros = cursor.fetchall()

        if not todos_os_carros:
            print("Nenhum carro cadastrado ainda.")
        else:
            for carro in todos_os_carros:
                print(f"ID: {carro[0]} | {carro[2]} {carro[1]} ({carro[3]}cv)")

    elif opcao == "3":
        print("Saindo do programa... Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")

conexao.close()