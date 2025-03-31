"""
Strings são uma sequência de caracteres: podem ser letras, símbolos, números e espaços.
Podemos representá-las de duas formas:
- Com aspas simples: 'texto'
- Ou com aspas duplas: "texto"
"""

nome = 'Lucas'
frase = "Aprender Python é divertido"

"""
Também podemos usar aspas triplas (simples ou duplas) para strings de múltiplas linhas:
"""

mensagem1 = """Olha, eu 
posso quebrar 
em várias linhas"""

mensagem2 = '''Também com
aspas 
simples'''

"""
Strings são imutáveis: isso significa que não podemos alterá-las após criá-las.
"""

nome = "Lucas"
# nome[0] = "R"  # ❌ Isso gera erro: strings são imutáveis

"""
Strings são como listas (ou matrizes) de caracteres: podemos acessar cada caractere usando índices.
"""

a = "olá mundo!"
print(a[1])  # Resultado: "l" (lembre-se: o índice começa em 0)

"""
Podemos verificar o comprimento de uma string com a função len():
"""

print(len(a))  # Resultado: 10

# Concatenação e multiplicação de strings

"""
Concatenação significa juntar strings usando o operador +.
OBS: O operador + não soma valores nesse caso, apenas junta.
"""

nome1 = "Lucas"
sobrenome1 = "Ulerich"

print(nome1 + " " + sobrenome1)  # Resultado: Lucas Ulerich

"""
Podemos multiplicar uma string com o operador * (como na matemática).
"""

nome2 = "Lucas"
print(nome2 * 4)  # Resultado: LucasLucasLucasLucas

# Formatação de strings

nome = "Lucas"
sobrenome = "Ulerich"
nome_completo = "Lucas Ulerich"

print("Nome completo: (1ª forma)", nome_completo)
print("Nome completo: (2ª forma) " + nome_completo)
print("Nome completo: (3ª forma) " + nome + " " + sobrenome)
print("Nome completo: (4ª forma) %s" % nome_completo)
print("Nome completo: (5ª forma) %s %s" % (nome, sobrenome))
print(f"Nome completo: (6ª forma) {nome_completo}")  # f-string (moderna e recomendada)

# Strns tem varios métodos embutidos

nome = "lucas"

print(nome.upper())     # LUCAS
print(nome.capitalize())# Lucas
print(nome.isalpha())   # True
print(nome.replace("a", "4"))  # luc4s
print(nome.startswith("lu"))  # True
print(nome.endswith("s"))     # True
print(nome.find("c"))         # 2 (posição)

txt = "Hello world"
txt = txt.upper()
print(txt)