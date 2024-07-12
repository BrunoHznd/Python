nota1 = float(input("Informe a nota 1"))
nota2 = float(input("informe a nota 2"))

media = (nota1 + nota2) / 2

if(media >= 7):
    print("A média: %.1f - Aprovado " % media);
else:
    print("A média: %1.f - Reprovado " % media);