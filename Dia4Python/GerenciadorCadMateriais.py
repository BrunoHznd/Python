lista_materiais = []

def cadastrarMateriais (nome, codigo, unidade, quantidade):
    tupla = (nome, codigo, unidade, quantidade)
    lista_materiais.append(tupla)
    return lista_materiais

def consultaMaterias (codigo):
    for material in lista_materiais:
        if material[1] == codigo:
            return print(material)
        else:
            print("nenhum item com esse codigo")

cadastrarMateriais("Borracha", 1, 'und.', 500)
cadastrarMateriais("Canetas", 25, 'und.', 250)
print(lista_materiais)
print("\n\n\n")
consultaMaterias(4)
