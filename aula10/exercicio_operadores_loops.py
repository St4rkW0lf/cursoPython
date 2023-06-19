for c in range(0, 5):
    sexo = input("Informe M para Masculino ou F para Feminino: ")

    if sexo == "M":
        print("Sexo masculino\n")
    else:
        print("Sexo feminino\n")

    nome = input('Informe o {c}º nome: ')

    idade = input('Informe a {c}ª idade: ')

    print('O {c} nome é: ', nome)
    print('A {c} idade é: ', idade)
