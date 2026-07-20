import sqlite3

# --- 1. Nossa classe de sempre ---
class Carro:
    def __init__(self, modelo, marca, potencia):
        self.modelo = modelo
        self.marca = marca
        self.potencia = potencia

# --- 2. Criando o objeto em Python ---
# Você pode mudar esses valores para o carro que você quiser!
meu_carro = Carro('Civic', 'Honda', 150)


# --- 3. Conectando e salvando o OBJETO no Banco ---
conexao = sqlite3.connect('oficina.db')
cursor = conexao.cursor()

# Garantimos que a tabela existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT,
        marca TEXT,
        potencia INTEGER
    )
''')

# INSERÇÃO DINÂMICA: Usamos "?" como marcadores para passar os atributos do objeto com segurança
cursor.execute('''
    INSERT INTO carros (modelo, marca, potencia)
    VALUES (?, ?, ?)
''', (meu_carro.modelo, meu_carro.marca, meu_carro.potencia))

conexao.commit()


# --- 4. Buscando e exibindo ---
cursor.execute('SELECT * FROM carros')
todos_os_carros = cursor.fetchall()

print("--- CARROS CADASTRADOS NO BANCO ---")
for carro in todos_os_carros:
    print(f"ID: {carro[0]} | {carro[2]} {carro[1]} ({carro[3]}cv)")

conexao.close()
