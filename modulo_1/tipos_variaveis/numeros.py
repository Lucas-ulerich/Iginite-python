# Inteiro

x = 10     # Inteiro positivo
y = -5     # Inteiro negativo
z = 0      # Zero
print("Numero inteiro ", x)

# Real com ponto flutuante

a = 3.14  # Número de ponto flutuante (float)
b = -0.001  # Número de ponto flutuante negativo
c = 2.0   # Apesar de ser um "2", como há um ponto decimal, é considerado float
print("Numero real ", a)

"""
Você pode usar a notação científica para representar números muito grandes ou muito pequenos:
"""

d = 1.2e3  # Equivalente a 1.2 * 10^3, ou 1200.0
e = 2.5e-4  # Equivalente a 2.5 * 10^-4, ou 0.00025
print("Numero real muito grande ",d)

print(type(e))

# Complex

"""
Python também oferece suporte a números complexos. Números complexos têm uma parte real 
e uma parte imaginária, representada pela letra j (ao invés de i, como na matemática).
"""
n = 2 + 3j  # Número complexo (parte real 2, parte imaginária 3j)
m = -5j     # Apenas a parte imaginária

# OPERÇÕES ARITIMÉTICAS

"""
Python suporta todas as operações matemáticas básicas e algumas operações avançadas. 
Aqui estão as principais operações que você pode fazer com números:
"""

f = 10
g = 3

# Adição (+)
print(f + g)  # Saída: 13

# Subtração (-)
print(f - g)  # Saída: 7

# Multiplicação (*)
print(f * g)  # Saída: 30

# Divisão (/)
print(f / g)  # Saída: 3.3333333333333335 (resultado float)

# Divisão inteira (//)
print(f // g)  # Saída: 3 (parte inteira da divisão)

# Módulo (%)
print(f % g)  # Saída: 1 (resto da divisão)

# Exponenciação (**)
print(f ** g)  # Saída: 1000 (10 elevado à potência de 3)
