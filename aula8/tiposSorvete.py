# Tipos de sorvete: fruta, leite, palito

tipoSorvete = str(input("Informe o tipo de sorvete: "))

if tipoSorvete == "fruta" or tipoSorvete == "frutas":
    print("Aqui vai um sorvete de frutas! :D")
elif tipoSorvete == "leite":
    print("Um sorvete de leite pra você! ^^")
elif tipoSorvete == "palito":
    print("Aqui, seu picolé! :)")
else:
    print("Não temos esse tipo de sorvete!")
