# LISTAS, TUPLAS E DICIONÁRIOS
# DICIONÁRIOS -> CADASTRO DE ALUNO

aluno = {
    'nome': input('Nome do aluno: '),
    'idade': input('Idade do aluno: '),
    'nota': input('Nota do aluno: ')

}

print(f"{aluno['nome']} tem {aluno['idade']} anos de idade e tirou uma nota de {aluno['nota']}")