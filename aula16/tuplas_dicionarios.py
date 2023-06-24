jogos = {}

for i in range(5):
    gname = input("Informe um jogo para adicionar a lista: ")
    jogos.update({i: gname})
    print(f'Jogo {gname} inserido!\n')
    print("Lista atual:\n", jogos)
    
print("Sua lista está completa!")
