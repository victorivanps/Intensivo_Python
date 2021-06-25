# Curso Intensivo de Python
# 23/06/2021 - UFOP - Eng. da Computação - Victor Ivan Piloto Santos
# Cap 3 Ex. 4

convidados = ['Eliane','Edvaldo','Esther','Khalil','Guilherme','Nelma']

del convidados[1]

convidados.insert(0,'Edvaldo')
convidados.insert(2,'Andre')
convidados.append('Gabriel')



for i in convidados:
  print("Encontrei uma mesa mais e estou convidando pessoas a mais.\nAguardo sua presença, "+i+".\nObrigado e boa noite!")