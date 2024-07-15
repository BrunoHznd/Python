#abre o arquivo se não tiver cria um
arquivo = open('arquivo.txt', 'w')

#escreve algo no arquivo
arquivo.write('Teste Python Criado usando função \n')
arquivo.write('Dia 3 Python')

#Fecha o arquivo
arquivo.close()

#lendo o arquivo
leitura = open('arquivo.txt', 'r')
print (leitura.read())

