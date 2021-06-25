# Curso Intensivo de Python
# 23/06/2021 - UFOP - Eng. da Computação - Victor Ivan Piloto Santos
# Cap 3 Ex. 7


convidados = ['Eliane','Edvaldo','Esther','Khalil','Guilherme','Nelma']

print("Olá galera, só posso convidar duas pessoas para o jantar nessa semana.")


cp = convidados.pop(1)
print("Desculpe, "+cp+" voce foi convidado(a) a sair da mesa dessa semana.")
cp = convidados.pop(1)
print("Desculpe, "+cp+" voce foi convidado(a) a sair da mesa dessa semana.")

del convidados[-1]
del convidados[-1]

for i in convidados:
  print("\nBoa noite, venho por essas más escritas linhas convida-los ao meu jantar.\nAguardo sua presença, "+i+".\nObrigado e boa noite!\n")