

numerosaleatorios = [5, 3, 30, 48, 54, 85, 22, 96, 75]

pares = list(filter(lambda x: x % 2 == 0, numerosaleatorios)) #usando a função lambda para filtrar os numeros pares
print(pares) 