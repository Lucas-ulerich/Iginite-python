# Fatiamento de strings

"""
O Fatiamento de strings serve para cortamos os caracteres em uma string.
"""

nome = "Lucas"

# Para realizar o fatiamento temos que colocar a posição inicial e a final.
# O indice sempre começa com 0

print(f"posições completas: {nome[2:4]}")

# Se deixarmos a posição inicial vazia, o python começara do primeiro caractere.
print(f"posições inicial vazia: {nome[:3]}")

# Mesma coisa vale pra posição final caso ela esteja vazia.
print(f"posições final vazia: {nome[2:]}")

# Indexação negativa
"""
Os índices negativos em Python são uma forma de contar de trás para frente os elementos de uma string.
A contagem com -1 representa o último caractere, -2 o penúltimo, e assim por diante.
Porém, mesmo usando índices negativos, o fatiamento ([início:fim]) é feito da esquerda para a direita por padrão.
Se colocarmos o índice inicial como -1 (último caractere) e o final como -3 (mais à esquerda), o Python tentará ir para frente — ou seja, da posição -1 até -3 — o que não faz sentido na ordem natural.
Como o início é depois do fim e o passo padrão é positivo, o resultado será uma string vazia.
Para que a leitura funcione nesse caso, é necessário usar um passo negativo (-1) que inverte a direção da leitura.
"""

print(f"Index negativo: {nome[-5:-2]}")
print(f"vazio, porque direção está invertida:  {nome[-1:-3]}")
print(f"funciona porque o passo é -1:  {nome[-1:-3:-1]}")



