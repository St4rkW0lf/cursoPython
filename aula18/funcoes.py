def percorre_tupla():
    
    for i in range(10):
        tupla = tuple(range(i))
        print(tupla)

def adiciona_item_dicionario(*valores):
    dicionario = {}

    for i, valor in enumerate(valores):
        chave = f'item_{i + 1}'
        dicionario[chave] = valor

    return dicionario

meu_dicionario = adiciona_item_dicionario('valor1', 'valor2', 'valor3')
print(meu_dicionario)

percorre_tupla()
