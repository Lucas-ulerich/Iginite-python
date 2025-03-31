import random

print('********************** DESAFIO 1 **********************')
'''
Desafio 1: Tipos e Identificação
Crie um programa que declare:

Uma variável com número inteiro

Uma variável com número decimal

Uma variável com número complexo

Depois, exiba o tipo de cada uma usando a função apropriada
'''

x = 10
y = 5.7
z = 3 + 2j

print(type(x))
print(type(y))
print(type(z))


print('********************** DESAFIO 2 **********************')
'''
Desafio 2: Simulando um Dado com random
Importe a biblioteca random.

Gere um número aleatório entre 1 e 6 (simulando um dado).

Exiba o número gerado.
'''
print(random.randrange(1,7))

print('********************** DESAFIO 3 **********************')
'''Desafio 3: Preço Aleatório com Duas Casas Decimais
Gere um número decimal aleatório entre 10 e 100.

Arredonde para duas casas decimais.

Mostre o valor formatado como um preço.'''

numero = random.randrange(10, 100)
print(float(numero))


print('********************** DESAFIO 4 **********************')
'''
Desafio 4: Conversão e Casting
Crie uma variável com valor decimal (float).

Converta para inteiro (int).

Exiba o valor antes e depois da conversão.
'''

numero1 = 5.78
print(numero1)
print(int(numero1))


print('********************** DESAFIO 5 **********************')
'''Desafio 5: Brincando com Números Complexos
Crie um número complexo.

Mostre a parte real e a parte imaginária separadamente.'''

numero_complex = 5 + 3j
print(numero_complex.real)
print(numero_complex.imag)


print('********************** DESAFIO 6 **********************')
'''Desafio 6: Jogo do Número Secreto
Gere um número aleatório entre 1 e 10.

Peça ao usuário para tentar adivinhar.

Mostre se ele acertou ou errou.'''

numero_digitado = input('Digite um numero de 1 a 10: ')
numero_aleatorio = random.randrange(1, 11)

numero_digitado = int(numero_digitado)

if numero_digitado == numero_aleatorio:
    print('Acertou, parabens')
else:
    print(f'Errou o numero era {numero_aleatorio}')


print('********************** DESAFIO 7 **********************')
''' Desafio 7: Operações com Tipos Diferentes
Crie três variáveis: uma int, uma float e uma complex.

Faça alguma operação com elas (soma, multiplicação...).

Exiba o resultado final e o tipo do resultado.'''

inteiro = 3
real = 3.14
complexo = 3 + 5j

soma = inteiro + real
subtracao = inteiro - complexo
multiplicacao = complexo * inteiro

print(soma)
print(subtracao)
print(multiplicacao)