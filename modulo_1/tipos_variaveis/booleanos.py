# Condição verdadeira
True

# Condição Falsa
False

# Condicionais

if True:
    print("Bloco IF vai ser executado")
else:
    print("Bloco ELSE nao sera executado")


# Operadores lógicos and e or

# AND
# Compara os dois valores, se os dois foram verdadeiro ele executa o bloco
if True and True:
    print("Bloco IF vai ser executado")

# Como uma das condições é falsa, o bloco não será executado
# O operador 'and' precisa que todas as comparações deem verdadeiro
if True and False:
    print("Bloco IF nao sera executado")

# OR
# O operador or precisa que pelo menos uma condição seja verdadeira pra executar o bloco.
if True or False:
    print("Bloco IF vai ser executado")

# Se as duas condições forem falsas o bloco não será executado.
if False or False:
    print("Bloco IF nao ser executado")