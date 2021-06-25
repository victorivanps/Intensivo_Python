# Curso Intensivo de Python
# 23/06/2021 - UFOP - Eng. da Computação - Victor Ivan Piloto Santos

print('1º Parte - Conceitos Iniciais')

# Lista é uma coleção de itens em uma ordem em particular.
#Ex: [a,b,c,d,e,f] ou [0,1,2,3,4,5,6,7,8,9]

# Não precisam estar relacionados de nenhum modo em particular.

bicycles = ['trek','cannondale','redline','specialized']

print(bicycles)


#Acessando os dados da lista
# Ex: 1º Item da lista bicycles

print(bicycles[0])

# O [0] representa o indice ou posição do item desejado.
# O [0] representa o 1º indice ou posição de uma lista.

# Ex: 2º e o 4º Item da lista bicycles

print(bicycles[1])
print(bicycles[3])

# Ex: Como acessar o ultimo item de uma lista

print(bicycles[-1])

# Retorna o valor 'specialized'. 
# print(bicycles[-2]) devolve o segundo item a partir do final da lista.

print('')
print('#########################################')
print('2º Parte - Inserção, Alteração e Exclusão')

#Alterando, acrescentando e removendo elementos

#As Listas são dinamicas, significando que podemos criar uma lista adicionando e removendo elementos dela.

motos = ['honda','yamaha','suzuki']
print(motos)

#Sobreescrevemos 'ducati' na posição 0 da lista motos, colocando no lugar de honda

motos[0] = 'ducati'
print(motos)

#Acrecentando elementos na lista
# Concatenando elementos no final de uma lista
# O elemento adicionado vai para o final da lista.

motos = ['honda','yamaha','suzuki']

motos.append('ducati')

print(motos)

#Inserindo elementos em uma lista
# Conseguimos adicionar um novo elemento em qualquer posição de sua ista usando o método insert().
# Especifique o indice do elemento e o valor.

motos.insert(0,'harley')
print(motos)


#Removendo elementos de uma lista
# Podemos remover um item de acordo com sua posição na lista ou seu valor.
# Removemos o 1º item da lista.
motos = ['honda','yamaha','suzuki']
print(motos)

del motos[0]
print(motos)

# É possivel remover qualquer item de uma lista usando o metodo del, desde que se saiba o seu índice.

#Removendo um item com o método Pop()
# Util para usar o valor de um item depois de removê-lo de uma lista.
# Permite trabalhar com esse item depois da remoção.
# Por padrão remove o ultimo.

motos = ['honda','yamaha','suzuki','harley']
print(motos)

ex = motos.pop()
print(motos)
print(ex)

# Pop() pode remover um item de qualquer posição de uma lista, se incluir o item que se deseja remover entre parenteses.

motos = ['honda','yamaha','suzuki','harley']
print(motos)

ex = motos.pop(2)
print(motos)
print(ex)

#Removendo item de acordo com o valor
# Não sabendo a posição do item, mas sabendo o seu valor é possivel remove-lo da lista.
# Usando o método remove()

motos = ['honda','yamaha','suzuki','harley']
print(motos)

motos.remove('yamaha')
print(motos)

print('')
print('#########################################')
print('3º Parte - Ordenação')

#Organizando uma lista
# As listas serão criadas em uma ordem imprevisível, pois nem sempre você poderá controlar a ordem em que seus usuários fornecem seus dados.
# Mesmos sendo inevitavel, python oferece várias maneiras de organizar suas listas de acordo com a situação.

#Ordenando com o Método sort()
#Suponhando que temos uma lista de carros e queremos alterar a ordem da lista para armazenar os itens em ordem alfabetica. 

carros = ['bmw','audi','toyota','subaru']
print(carros)
carros.sort()
print(carros)

# Preservando a ordem original de uma lista, mas apresentando-a de forma ordenada, usamos a função sorted().

carros = ['bmw','audi','toyota','subaru']
print('Lista Original')
print(carros)

print('Lista Ordenada')
print(sorted(carros))

print('Lista')
print(carros)

# Exibindo a lista em ordem inversa

carros = ['bmw','audi','toyota','subaru']
print('Lista Original')
print(carros)

carros.reverse()
print('Lista Invertida')
print(carros)

# O metodo reverse muda a ordem de uma lista de forma permanente, mas conseguimos retorna-la ao normal usando o reverse novamente.

# Descobrindo o tamanho de uma lista
#Utilizamos o metodo len().
#É util para descobrir a contagem de dados que existem em uma lista.
carros = ['bmw','audi','toyota','subaru']
print('Itens na lista de carros: '+ str(len(carros)))

print('')
print('#########################################')
print('4º Parte - Evitando erros com indices')

# Um erro comum quando trabalhamos com lista pela primeira vez.

#motos = ['honda','yamaha','suzuki']
#print(motos[3])

# Rodando esse codigo dá erro, já que o indice 3 representa o 4 item da lista, que não existe.
# Para acessar o ultimo item da lista use o indice -1

motos = ['honda','yamaha','suzuki']
print(motos[-1])

# Caso a lista seja vazia e não há indices, se tentarmos retornar o ultimo item da lista, existe outro erro de indice.