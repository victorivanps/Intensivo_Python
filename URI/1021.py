# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.


#Está dando erro até o seguinte momento.

x = float(input())

if x>=0 and x<=1000000.00:
    notas = [100.00,50.00,20.00,10.00,5.00,2.00,1.00,0.5,0.25,0.10,0.05,0.01]
    r = []

    for i in range(0,len(notas)):
        y = int(x/notas[i])
        r.append(y)
        x = x%notas[i]

    print('NOTAS:')
    for i in range(0,6):
        print(str(int(r[i])) + ' nota(s) de R$ %.2f' % notas[i])

    print('MOEDAS:')
    for i in range(6,12):
        print(str(int(r[i])) + ' moeda(s) de R$ %.2f' % notas[i])

    
