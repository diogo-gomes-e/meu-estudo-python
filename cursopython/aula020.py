# Aggregation p/2 (exercicio)

class Livro:
    def __init__(self, autor, titulo, paginas, status):
        self.autor = autor
        self.titulo = titulo
        self.paginas = paginas
        self.status = status

    def verificar_status(self):
        return "Disponível" if self.status else "Indisponível"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f'Autor: {livro.autor} - Título: {livro.titulo} - Paginas: {livro.paginas} Status: {livro.verificar_status()}')
# Criando os Objetos
livro1 = Livro(autor='William Shakespeare', titulo='Romeu e Julieta', paginas=400, status=True)
livro2 = Livro(autor='Jane Austen', titulo='Orgulho e Preconceito', paginas=200, status=True)
livro3 = Livro(autor='Machado de Assis', titulo='Dom Casmurro', paginas='500', status=False)
livro4 = Livro(autor='Gabriel García Márquez', titulo='Cem anos de solidão', paginas=300, status=True)

# Criar a biblioteca e adicionar os livros
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

# Listar os livros (Usando o objeto Biblioteca!)
biblioteca.listar_livros()
