"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia =

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.


Exemplo de Entrada	
1.0 7.0
5.0 9.0

Exemplo de Saída
4.4721
"""

#Raiz Quadrada de 9 -> print(9 ** (1/2))
p1 = str(input('Informe os eixos x e y do ponto1 ')).split()
x1 = float(p1[0])
y1 = float(p1[1])
p2 = str(input('Informe os eixos x e y do ponto2: ')).split()
x2 = float(p2[0])
y2 = float(p2[1])

#print(f'p1({x1}, {y1})')
#print(f'p2({x2}, {y2})')
distância = ((x2 - x1)**2 + (y2 - y1)**2 ) ** (1/2)
print(f'{distância:.4f}')



