"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Entrada	
556
Exemplo de Saída
0:9:16
"""

'''
t = int(input('Informe o tempo em segundos: '))
h = t // 3600
m = t // 60
s = t - (h * 3600) - (m * 60)
print(f'Segundos informado: {t}')
print(f'Tempo (horas:minutos:segundos) -> {h}:{m}:{s}')
'''


s = int(input())
h = s // 3600
m = s // 60
s = s - (h * 3600) - (m * 60)
print(f'{h}:{m}:{s}')
