import random

preco = random.uniform(10.00, 100.00)
preco = round(preco, 2)

desconto = random.randrange(5, 30)
preco_final = preco - (desconto * preco / 100)
codigo_pedido = random.randrange(1000, 9999)
codigo_pedido = str(codigo_pedido)

print(f'O preço do produto é: R$ {preco:.2f}', type(preco))
print(f'O desconto foi de: {desconto}%', type(desconto))
print(f'O preço final foi de: {preco_final:.2f}', type(preco_final))

resposta = input('Deseja comprar o item? ')

if resposta == 'sim':
    print('Compra realizada com sucesso!')
    print(f'Seu codigo pedido foi: {codigo_pedido}')
elif resposta == 'nao':
    print('Quem sabe na proxima')
else:
    print('Resposta incorreta.')



