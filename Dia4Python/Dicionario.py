emails_bruno = {

    "Principal": "bruno.carvalho@gmail",
    "Fatec": "Bruno.Carvalho888@fatec.sp.gov.br",

}

#buscando valor especifico
email = emails_bruno['Principal']
print(email)

#adicionando novo item no dicionario
emails_bruno["Secundario"] = "bruno.carvalho@hotmail.com"
print(emails_bruno)

# percorrendo todo o dicionario pegando somente as chaves
for emails in emails_bruno:
    print("todos os email do Bruno são: ", emails)

print(emails_bruno.keys())

print("\n\n\n")
#pegando os valores
for Imails in emails_bruno:
    email = emails_bruno[Imails]
    print(email)

print("\n\n\n")
#pegando pelo values
print(emails_bruno.values())

#retirando um item
emails_bruno.pop("Secundario")
print(emails_bruno)

print("\n\n\n")
#verificando somente pela chave se existe o email
if "Secundario" in emails_bruno:
    print("Existe")
else:
    print("não existe")
