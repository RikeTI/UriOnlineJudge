"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a + b + abs(a-b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada	
7 14 106

217 14 6

Exemplos de Saída
106 eh o maior

217 eh o maior
"""
#Lógica de Programação

# a = 106 ; b = 14 ; maior = 0
# MaiorAB = (a + b + abs(a-b)) / 2
# MaiorAB = (106 + 14 + abs(106-14)) / 2
# MaiorAB = (120 + abs(92)) / 2
# MaiorAB = (212) / 2
# maior = MaiorAB


n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])

MaiorAB = (a + b + abs(a-b)) // 2
Maior = (MaiorAB + c + abs(MaiorAB-c)) // 2
print('{} eh o maior'.format(Maior))
