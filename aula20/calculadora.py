def calculate(valor1, valor2):
    print("===== Bem-vind@ a calculadora simplificada em Python =====\n")
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
    choice = input("Que operação deseja realizar? ")
    
    if(choice == "1"):
        return print("Seu resultado é: ",valor1 + valor2)
    elif(choice == "2"):
        return print("Seu resultado é: ",valor1 - valor2)
    elif(choice == "3"):
        return print("Seu resultado é: ",valor1 * valor2)
    elif(choice == "4"):
        return print("Seu resultado é: ",valor1 / valor2)
    else:
        print("Opção inválida")

print("Olá, usuário! Para iniciar o programa, digite dois valores iniciais.")
v1 = float(input("Primeiro valor: "))
v2 = float(input("Segundo valor: "))

calculate(v1, v2)
