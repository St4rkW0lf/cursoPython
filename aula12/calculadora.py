operacao = ''
while operacao == '0':
    print("Escolha uma das opções:\n + -> Somar\n - -> Substrair\n * -> Multiplicar\n / -> Dividir\n 0 -> Sair")

    opcao = input("\nDigite aqui: ")
    if opcao == '0':
        print("Finalizando...")
        sleep(2)
        exit()

    n1 = input("Informe o primeiro número:\n")
    n2 = input("Informe o segundo número:\n")

    if opcao == '+':
        soma = n1 + n2
        print("A soma dos valores é:", soma, "\n")
        sleep(2)
    elif opcao == '-':
        subtracao = n1 - n2
        print("A subtração dos valores é:", subtracao, "\n")
        sleep(2)
    elif opcao == '*':
        multiplicacao = n1 * n2
        print("A multiplicação dos valores é:", multiplicacao, "\n")
        sleep(2)
    elif opcao == '/':
        divisao = n1 / n2
        print("A divisão dos valores é:", divisao, "\n")
        sleep(2)
    else:
        print("Informe uma opção válida!\n")
        sleep(2)
