"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

Exemplos de Entrada	
12 1 5.30
16 2 5.10
Exemplos de Saída
VALOR A PAGAR: R$ 15.50
"""
#Código da Peça, Número de Peças e o Valor Unitário da Peça
peça1 = input('Informe o Código da Peça I, o Número de Peças I e o Valor Unitário: ').split()
peça2 = input('Informe o Código da Peça II, o Número de Peças II e o Valor Unitário: ').split()
cp1 = int(peça1[0])
np1 = int(peça1[1])
vp1 = float(peça1[2])

cp2 = int(peça2[0])
np2 = int(peça2[1])
vp2 = float(peça2[2])

'''print(peça1)
print(cp1, type(cp1))
print(np1, type(np1))
print(vp1, type(vp1))
print()
print(peça2)
print(cp2, type(cp2))
print(np2, type(np2))
print(vp2, type(vp2))
'''
total = (np1 * vp1) + (np2 * vp2)
print('VALOR A PAGAR: R$ {:.2f}'.format(total))




