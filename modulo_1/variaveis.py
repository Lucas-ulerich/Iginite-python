# Por convenção usamos o padrão snake_case para nomear variaveis
nome_completo = "Lucas Ulerich"
saldo_total = 1.900


# Variaveis são case sensitive, ou seja uma variavel escrita em maiuscula é diferente de uma escrita em minuscula

idade = 25
Idade = 30  # Estas são duas variáveis diferentes

# Diferente do Java, no pynthon não precisamos colocar o tipo da variavel
# Python possui uma tipagem dinâmica.

numero = 10      # número inteiro
numero = 10.5    # Agora é um número decimal (float)
numero = "dez"   # Agora é uma string

# Podemos atualizar o valor de uma variavel.
x = 5  # Inicialmente, x é 5
x = 10  # Agora x é 10
print(x)  # Saída: 10

# Variável global
x = 10

def funcao():
    # Variável local
    y = 5
    print(x)  # Acessa a variável global
    print(y)  # Acessa a variável local

funcao()

print(x)  # Acessa a variável global
print(y)  # Isso vai gerar um erro, porque y é local e não existe fora da função

# Em python não tem forma oficial de decalrar constantes, mas por convenção usamos letras maiusculas.

PI = 3.14159
print(PI)  # Saída: 3.14159

# Modificando o valor de PI
PI = 3.14  # Tecnicamente, Python permite isso, mas é uma má prática
print(PI)  # Saída: 3.14


"""
- Variáveis são usadas para armazenar dados.
- Python permite tipagem dinâmica (o tipo de dado é determinado automaticamente).
- Variáveis podem ser reutilizadas e alteradas.
- Nomes de variáveis são sensíveis a maiúsculas e minúsculas.
- Variáveis podem ser globais ou locais, dependendo de onde são definidas.
- Em Python, não há uma palavra-chave ou mecanismo nativo para definir variáveis como constantes.
- A convenção para constantes é usar letras maiúsculas.
- Apesar de você poder modificar essas "constantes", a convenção sugere que essas variáveis não devem ser alteradas.
- Para organização e melhor isolamento, você pode definir constantes em módulos separados ou usar classes para agrupá-las.
"""

nome = "Lucas" # Tipo STRING
idade = 29 # Tipo NUMBER
altura = 1.62 # Tipo FLOAT, usa ponto ao inves de virgula
atleta = True # Tipo BOOLEAN