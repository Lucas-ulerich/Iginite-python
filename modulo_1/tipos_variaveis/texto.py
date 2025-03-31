# Declaração

nome_completo = "Lucas Ulerich" # É uma string

nome_completo_aspas = """Lucas 
Ulerich""" # para quebra de linha

nome_completo_quebra = "Lucas \
Ulerich" ## Usamos a barra para fazer a quebra de linha

nome = "Lucas"
sobrenome = "Ulerich"

numero = 123

#FORMATAÇÃO
print("Nome Completo:", nome_completo) # 1a forma de formatar (A virgula já coloca um espaço na frente)

print("Nome Completo:" + nome_completo) # 2a forma de formatar (Só funciona com strings)

print("Nome Completo:" + "Lucas" + "Ulerich") # 3a forma de formatar (Só funciona com strings, pois se usar o sinal de + em int ou float o python tentará somar)

print("Nome Completo:"+ "Lucas", "Ulerich") # 4a forma de formatar (Só funciona com strings)

print("Nome Completo:", nome_completo_aspas) # 5a forma de formatar (Só funciona com strings)

print("Nome Completo:", nome_completo_quebra) # 6a forma de formatar (Só funciona com strings)

print("Nome Completo: %s %s" %nome_completo_quebra) # 7a forma de formatar (Só funciona com strings)
print("Nome Completo: %s %s" %(nome_completo_quebra, numero)) # 7a forma de formatar (Para usar mais de uma variavél temos que colocar mais de um %s e colcoar as variaveis dentro de () e separadas por virgula.)

print(f" Nome completo: {nome_completo_aspas}, {nome_completo_quebra}") # 8a forma de formatar (Só funciona com strings)