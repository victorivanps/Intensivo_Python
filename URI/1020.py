# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.

x = int(input())

ano = [365,30,1]
res = []
for i in range(0,3):
    h = int(x/ano[i])
    res.append(h)
    x = x%ano[i]

print(str(res[0]) + ' ano(s)')
print(str(res[1]) + ' mes(es)')
print(str(res[2]) + ' dia(s)')


x = int(input())

tempo = [31104000,2592000,86400,3600,60,1]

res = []

for i in range(0,6):
    t = int(x/tempo[i])
    res.append(t)
    x = x%tempo[i]

print(str(res[0])+'/'+str(res[1])+'/'+str(res[2]))
print(str(res[3])+':'+str(res[4])+':'+str(res[5]))