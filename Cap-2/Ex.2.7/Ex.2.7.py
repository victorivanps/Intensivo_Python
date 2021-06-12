# Curso Intensivo de Python
# 12/06/2021 - UFOP - Eng. da Computação - Victor Ivan Piloto Santos
# Cap 2 Ex. 7: Armazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do nome. 
# Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
# Exiba o nome uma vez, de modo que os espaços em branco em torno do nome sejam mostrados.
# Em seguida, exiba o nome usando cada uma das três funções de emoção de espaços: lstrip(), rstrip() e strip().

nome = "     Victor Ivan Piloto Santos"

print(nome)

print(nome.rstrip())
print(nome.lstrip())
print(nome.strip())
