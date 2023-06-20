lista = []

for i in range(10):
    produto = input("Insira um produto na sua lista de compras, ou, digite S para sair do programa\n")
    
    if produto == "S" or produto == "s":
        print("Finalizando programa...")
        break
    
    else:
        lista.append(produto)
        print("Lista atual: ")
        print(lista, "\n")
        
print("Sua lista final: ", lista)
