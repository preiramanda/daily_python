# *args and **kwargs

def add(*args):
    n = 0
    for i in args:
        n += i
    return n

add(5,6,7)


def minha_funcao(*args, **kwargs):
    print("Argumentos posicionais (*args):")
    for arg in args:
        print(arg)
    
    print("\nArgumentos de palavra-chave (**kwargs):")
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

minha_funcao('a', 'b', 'c','d', 'Alice', 30, 'São Paulo',nome=80, )
