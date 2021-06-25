# Curso Intensivo de Python
# 23/06/2021 - UFOP - Eng. da Computação - Victor Ivan Piloto Santos
# Cap 3 Ex. 7

locais = ['Turquia','Canada','Japão','Tailandia','Grecia']
print(locais)

print('\nOrdenada')
print(sorted(locais))

print('\nOrdenada Inversa')
print(sorted(sorted(locais)))

print('\nLista Inversa')
locais.reverse()
print(locais)

print('\nLista Ordenada Definitiva')
locais.sort()
print(locais)

print('\nLista Ordenada Inversa Definitiva')
locais.reverse()
print(locais)