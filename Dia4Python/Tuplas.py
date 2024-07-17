#criando uma tupla
#diferença entre tupla e lista: Lista permite alteração tupla não
tupla = (1,2,3,4,5, "Bruno")
print(tupla[3])

#lista de Tuplas
cliente = ("Bruno", '123.145.154-88', '45,468,498-8')
clientes = []
clientes.append(cliente)
print(clientes)

#por terem dados diferentes as tuplas nao necessariamente precisam de nomes diferentes
cliente = ("Hhhhznd", '288.468.465-78', '325.651.322-1')
clientes.append(cliente)
print(clientes)
#printando cliente especifico
print(clientes[1])

print("\n\n\n")

#tuplas com chaves de dicionarios
capitais =  {

    ('Brasil', 'Rio De Janeiro'): 'Rio De Janeiro',
    ('Brasil', 'São Paulo'): 'São Paulo',
    ('Brasil', 'Minas Gerais'): 'Belo Horizonte'

}

print(capitais.keys())
print(capitais.values())


print("\n\n\n")
tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
#Buscando valor na tupla
print(tupla.index(15))
#Informa quantidade de vezes de um dado repetido
print(tupla.count(3))
