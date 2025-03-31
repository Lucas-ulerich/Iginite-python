# Em Python, o tipo de dado é definido quando você atribui um valor a uma variável:

x1 = 'Hello World'
x2 = 20
x3 = 20.5
x4 = 1j
x5 = ["apple", "banana", "cherry"]
x6 =  ("apple", "banana", "cherry")
x7 = range(6)
x8 = {"apple", "banana", "cherry"}
x9 = frozenset({"apple", "banana", "cherry"})
x10 = True
x11 = b'Heloo'
x12 = bytearray(5)
x13 = memoryview(bytes(5))
x14 = None


# Você pode obter o tipo de dados de qualquer objeto usando a type()função:
x = 5
print(type(x))

# Se você quiser especificar o tipo de dados, poderá usar as seguintes funções construtoras:

x1 = str('Hello World')
x2 = int(20)
x3 = float(20.5)
x4 = complex(1j)
x5 = list(("apple", "banana", "cherry"))
x6 =  tuple(("apple", "banana", "cherry"))
x7 = range(6)
x8 = dict(("apple", "banana", "cherry"))
x9 = frozenset({"apple", "banana", "cherry"})
x10 = bool(5)
x11 = bytes(5)
x12 = bytearray(5)
x13 = memoryview(bytes(5))
x14 = None