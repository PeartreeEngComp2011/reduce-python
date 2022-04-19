#Função reduce

#Importando a função
from functools import reduce

def soma(x,y):
	return x+y

lista = [1,3,5,7,9,11,13,15]

soma = reduce(soma,lista)

print(soma)