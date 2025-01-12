nums = [5,3,6,8,9]

print(type(nums)) # para mostrar o tipo da estrutura

nums.append(7) #para adicionar um elemento no final da lista
print(len(nums)) # para ver a quantidade de elementos dentro da lista
nums[3] = 80 # para substituir a posição 3 com o numero 80
nums.insert(2, 90)#para inserir o 90 na posição 2 da lista
print (nums)
print (nums[-1]) #para acessar o penultimo da lista
nums.pop() #para tirar o ultimo da lista
print(nums) 
print (nums[0:3])#do lado esquerdo dos dois ponto para acessar o inicio e do lado direiro o fim do acesso a lista
