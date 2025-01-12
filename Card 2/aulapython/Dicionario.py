aluno = {
    'nome' : 'leo',
    'Idade' : 18,
    'especialidade' : 'cientista de dados',
    'cidade' : 'santa helena'
}

print(aluno)
print(aluno['nome']) # mostrei a chave especifica
aluno['país'] = 'tupã' #adicionei um chave e elemento no dicionario
print(aluno)
del aluno['país'] # deletar um chave e valor do dicionario
print(aluno)

