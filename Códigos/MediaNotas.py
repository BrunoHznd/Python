def lernotas():
    n = float(input('Digite uma nota para o aluno: \n' ))
    return n


def resultado(n1,n2):
    media = (n1 + n2) / 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "Resultados: ", end=" ")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")



a = lernotas()
b = lernotas()
resultado(a,b)