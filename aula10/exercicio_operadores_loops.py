for c in range(0, 5):
    sexo = input("Informe M para Masculino ou F para Feminino: ")

    if sexo == "M":
        print("Sexo masculino\n")
    else:
        print("Sexo feminino\n")

    nome = input(f'Informe o {c}º nome: ')

    idade = input(f'Informe a {c}ª idade: ')

    print(f'O {c} nome é: ', nome)
    print(f'A {c} idade é: ', idade)
