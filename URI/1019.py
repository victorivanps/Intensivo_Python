# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

x = int(input())

tempo = [3600,60,1]
res = []
for i in range(0,3):
    h = int(x/tempo[i])
    res.append(h)
    x = x%tempo[i]

print(str(res[0])+':'+str(res[1])+':'+str(res[2]))