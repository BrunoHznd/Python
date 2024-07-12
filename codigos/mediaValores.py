qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor:"))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    #entrada dos Valores
    valor = float(input("Digite um valor"))

#caso digite um valor negativo o laço encerra
media = soma / qtd
print("\n total da Soma: ", soma)
print("\n Quantidade de valores digitados: ",qtd)
print("\n media dos valores: ", media)