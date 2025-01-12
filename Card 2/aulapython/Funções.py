from functools import reduce

def saudação():
    print('boa tarde') #uma função que vai retornar um print

saudação()

def saudação1(nome):
    print(f'bom dia, {nome}')  # aqui mostra uma função que com parametros de entrada


saudação1('maria')


nota = [8.8, 3.1, 5.5]

def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar

notas_finais = list(map(somar_nota(1.5), nota))  # ultilizandio o map para copiar a lista e alterar os valores atraves da função
print(notas_finais) 

numeros = [5, 3, 1, 4, 7]

def somar(a,b):
    return a + b

resultado = reduce(somar, numeros, 0)
print(resultado)