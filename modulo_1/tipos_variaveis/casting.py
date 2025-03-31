'''
Typecasting => É o processo de converter o tipo de dado de um objeto para outro
Em python temos dois tipos de conversão, a implícita e a explicita.
'''

# Conversão implícita
'''
Quando o próprio interpretador do python realiza a conversão
OBS: Ele vai sempre evitar a perda de dados, então sempre converterá para um tipo de dados maior
'''

numero_inteiro = 10
numero_real = 1.23

print(numero_inteiro ,type(numero_inteiro))
print(numero_real, type(numero_real))

soma = numero_inteiro + numero_real

print(soma, type(soma)) # A soma é um float

# O python numca converterá um int ou um float para ‘string’, caso tente dara erro!!

numero_inteiro = 10
texto_string = '12'

# soma = numero_inteiro + texto_string -> Ira causar o erro "TypeError: unsupported operand type(s) for +: 'int' and 'str'"

# Conversão explicita

'''
Podemos forçar a conversão usando os métodos do python:

int() -> Para converter para o tipo inteiro
float() -> Para converter para o tipo real
str() -> Para converter para o tipo string
bool() -> Para converter para o tipo booleano
complex() -> Para converter para o tipo complexo
'''

numero_inteiro = 123
numero_real = 1.23

numero_inteiro = float(numero_inteiro)
print(f'O numero inteiro agora é um numero real: {numero_inteiro}, {type(numero_inteiro)}')

soma_numeros = numero_inteiro + numero_real

print(f'A Soma será um numero real: {soma_numeros}, {type(soma_numeros)}')

# Agora que a string foi convertida para inteiro, podemos somar normalmente.

outro_inteiro = 123
numero_texto = '12'

print(f'Perceba que até esse momento ele é um texto: {numero_texto}, {type(numero_texto)}')

numero_texto = int(numero_texto)
print(f'Agora ele é um inteiro: {numero_texto}, {type(numero_texto)}')

# podemos somá-los

soma_estranha = outro_inteiro + numero_texto
print(soma_estranha, type(soma_estranha))

# Forçando a perda de dados

inteiro = 123
real = 1.34

# com essa conversão perdemos a parte fracionaria do número.
real = int(real)

perda = inteiro + real
print (f'perdemos o .34 do número: {perda, type(perda)}')
