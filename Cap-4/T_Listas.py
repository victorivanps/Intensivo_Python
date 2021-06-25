# Curso Intensivo de Python
# 23/06/2021 - UFOP - Eng. da Computação - Victor Ivan Piloto Santos

print('1º Parte - Conceitos Iniciais')
# Nesse capitulo é trabalhado o listas mas com laços repetitivos, permintindo percorrer um laço de uma maneira melhor. Pois permite executar um conjunto de ação em todos os itens de uma lista.

#Percorrendo a lista inteira com o laço

magicos = ['alice','david','carolina']
for magico in magicos:
  print(magico)

print('#######################################################')
# A linha 9 é criada a lista de magicos
# A linha 10 é criado o laço dizendo o seguinte: Extraia um item da lista magicos e guarde-o em magico
# A linha 11 é usado o print, para mostrar o item na tela. Exibindo uma vez para cada item na lista.
# print('#######################################################')
# Testes
# num = [0,1,2,3,4,5,6,7,8,9]
# soma = 0
# for i in num:
#   soma +=i
# print(soma)
# print('#######################################################')
# Fim do Teste
# 
# Executando mais tarefas em um laço for
# Podemos Fazer praticamente tudo com cada item em um laço for.

magicos = ['alice','david','carolina']
for magico in magicos:
  print(magico.title() + ", isso foi um grande truque!")

print('\n#######################################################')
# Podemos escrever tantas linhas de código possivei no laço for, desde que toda linha identada após a 
# linha: for ... in ...: 
#   esteja dentro do laço, e cada linha indentada é executada uma vez para cada valor da lista.

magicos = ['alice','david','carolina']
for magico in magicos:
  print("\n" + magico.title() + ", isso foi um grande truque!")
  print('Não consigo esperar pelo proximo truque do(a), ' + magico.title())

print('\n#######################################################')

# Fazendo algo após um laço for
# Qualquer codigo após o laço for que não estiver indentada será executada uma vez, sem repetição.

magicos = ['alice','david','carolina']
for magico in magicos:
  print("\n" + magico.title() + ", isso foi um grande truque!")
  print('Não consigo esperar pelo proximo truque do(a), ' + magico.title())
print("\nObrigado pessoal. Esse foi um grande show de magica!!")

print('\n#######################################################')

print('2º Parte - Listas Numericas\n')
# Listas são ideais para se guardar um conjunto de numeros e Python oferece várias ferramentas para ajudar nesse trabalho.

#Usando a função range()
# Gera uma serie de numero em uma sequencia.

for i in range(1,5):
  print(i)
print('\n#######################################################')
# O nº 5 não aparece pois Python começa a contar no primeiro valor que é fornecido e para de contar quando atinge o segundo numero fornecido.

# Usando range() para criar uma lista de números
# Podemos converter os resultados da função range() em uma lista rapidamente utilizando a função list().

numeros = list(range(1,10))
print(numeros)
print('\n#######################################################')
# Podemos utilizar para só usar a função range em uma determinada sequencia de numeros.

impares = list(range(1,10,2))
print(impares)
pares = list(range(2,11,2))
print(pares)
print('\n#######################################################')
# Impares, cria uma lista de numero de 1 até 9 pulando 2 em 2 numeros.
# Pares, cria uma lista de numero de 2 até 10 pulando 2 em 2 numeros.

# Pode-se criar qualquer lista de numeros com a função range()

quadrados = []
for i in range(1,11):
  quadrados.append(i**2)
print(quadrados)
print('\n#######################################################')
# Concentre-se primeiro em escrever um código que você entenda claramente e faça o que vcocê quer que ele faça. Depois procure otimizar o codigo.

# Estatíticas simples com uma lista de números
# Algumas funções são específicas para listas de números.
# Pode-se encontrar facilmente o valor mínimo, maximo e a soma de uma lista de números;

numeros = list(range(1,21))

print(min(numeros))
print(max(numeros))
print(sum(numeros))

print('\n#######################################################')
# List Comprehensions
# Combina o laço for e a criação de novos elementos em uma linha, e concatena cada novo elemento automaticamente.

quadrados = [i**2 for i in range(1,10)]
print(quadrados)
print('\n#######################################################')
# Usando essa sintaxe, você deve prestar atenção no nome da lista bem  e em seguida insira um colchete de abertura e defina a expressão para os valores que você quer armazenar na nova lista.

print('Parte 3º - Trabalhando com parte de uma lista')

# Fatiando uma lista
# Para criar uma fatia, especifique o indice do primeiro e do ultimo elemento com os quais vai ser trabalhado.

jogadores = ['charles','martina','michael','florence','eli']
print(jogadores[0:3])
print(jogadores[1:4])
print('\n#######################################################')

