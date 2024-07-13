idade = int(input("Informe a sua idade"))

if idade >= 0 and idade <= 10:
    print("Criança")
elif idade >= 11 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 55:
    print("Adulto")
elif idade > 55:
    print("veio")
else:
    print("Idade invalida")  