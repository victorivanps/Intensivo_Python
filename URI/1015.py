# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

# Distancia =

# Entrada
# O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída
# Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.


import math

pi = input()
pj = input()
p1 = []
p2 = []

for i in range(0,len(pi)):
    if pi[i] == ' ':
         index = i
         p1.append(float(pi[0:i]))
         p1.append(float(pi[i:len(pi)]))

for i in range(0,len(pj)):
    if pj[i] == ' ':
         index = i
         p2.append(float(pj[0:i]))
         p2.append(float(pj[i:len(pj)]))
distancia = 0
for i in range(0,2):
    distancia += ((p2[i] - p1[i])**2)

distancia = math.sqrt(distancia)

print(p1)
print(p2)
print('%.4f' % distancia)