alunos = ("leo","kaka","CR7", "vinijr")

print("vinijr" in alunos) #verifica se o elemento esta na tupla
print(alunos[0:1]) #para mostrar o elemento 1
print(alunos[0:]) # para mostrar do 1 ao ultimo da tupla
print(alunos[-1]) # para mostrar o ultimo na tupla 
print(type(alunos))  #par verificar o tipo da estrutura 
print(len(alunos))  #para verificar a quantidade de elementos na tupla

nota = [8.8, 3.1, 5.5]

def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar

notas_finais = list(map(somar_nota(1.5), nota))  # Convertendo o objeto map em uma lista
print(notas_finais) 