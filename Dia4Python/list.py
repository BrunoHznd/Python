#case 1
lista_precos = [500, 1500, 2000, 100, 25]

nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)
print(nova_lista_precos)

#case 2
nova_lista_precos2 = [preco * 2 for preco in lista_precos]
print(nova_lista_precos2)


#colocando o valor pela metade
lista_precosMenos = []
for preconeg in lista_precos:
    lista_precosMenos.append(preconeg / 2)
print(lista_precosMenos)


#caso imposto
imposto = []
for precoImpost in lista_precos:
    if precoImpost > 1000:
        imposto.append(precoImpost * 0.5)
print(imposto)


#list comprehension Imposto
imposto2 = [preco * 0.5 for preco in lista_precos if preco > 1000]
print(imposto2)

print("\n\n\n")

ListaTeste = [100,500,1000,5000,10000]

listaTestando = []
for NewListTest in ListaTeste:
    if NewListTest < 250:
        print("Número menor que 250")
    elif NewListTest > 250 and NewListTest < 1000:
        print("Numero maior que 250 e menor que 1000")
    elif NewListTest >= 1000:
        print("Maior ou igual a 1000")
    else:
        print("Seila")


