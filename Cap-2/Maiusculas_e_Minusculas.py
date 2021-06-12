# Curso Intensivo de Python
# 12/06/2021 - UFOP - Eng. da Computação - Victor Ivan Piloto Santos
# Apresentação de metodo para tornar as letras em maiusculas e minusculas

ex = "victor ivan"

# O metodo .title() atua emcima da variavel 'ex', exibindo cada palavra com uma letra maiuscula no inicio.
print(ex.title())

ex2 = "chapelzinho foi a casa do chapeleiro magico na fortaleza vermelha."

print(ex2.title())
##########################################################################################################

ex = "Victor Ivan Piloto Santos"

# .upper() faz com que todas as letras fiquem maiusculas
print(ex.upper())
# .lower() faz com que todas as letras fiquem minusculas
print(ex.lower())

##########################################################################################################

primeiro_nome = "Victor Ivan" 
ultimo_nome = "Piloto Santos"

# Operador '+' em String, cocatena as Strings e até variaveis que são String
nome_completo = primeiro_nome + " " + ultimo_nome

mensagem = nome_completo = "Ola, " + nome_completo + "!"

print(mensagem)

##########################################################################################################

# Tabulação 'tab' um breakspace maior que o normal

print("Victor\tIvan")

# Quebra de linha 'Enter' em textos

print("1 - Computadores\n2 - Mouses\n3 - Teclados\n4 - Mousepads\n")

##########################################################################################################

# Retirando espaços vazios em uma string

# .rstrip() - Retira espaço vazio a direita da string (temporariamente)

ex = "Victor Ivan "

print(ex.rstrip())

# .lstrip() - Retira espaço vazio a esquerda da string (temporariamente)

ex = " Victor Ivan"

print(ex.lstrip())

# .strip() - Retira espaço vazio a esquerda e a direita da string (temporariamente)

ex = " Victor Ivan "

print(ex.strip())

# Caso seja necessario manter a operação de retirada do espaço vazio, faça com que a variavel receba ela mesma com a operação

ex = " Victor Ivan "

ex = ex.strip()

print(ex)
